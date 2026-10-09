from unittest import mock

from django.core.cache import cache
from django.test import TestCase, override_settings

LOCMEM = {'default': {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}}


def make_disease(name):
    """Smallest Disease the page can render: every required section with empty text."""
    from polyQ import models as m
    sec = dict(identifier=name, text='')
    return m.Disease.objects.create(
        name=name, slug=f'{name} full name',
        introduction=m.Introduction.objects.create(**sec),
        first_described=m.FirstDescribed.objects.create(**sec),
        epidemiology=m.Epidemiology.objects.create(**sec),
        causative_gene=m.CausativeGene.objects.create(**sec),
        codified_protein=m.CodifiedProtein.objects.create(**sec, protein_functions='', protein_location=''),
        patho_physiology=m.PathoPhysiology.objects.create(**sec),
        clinical=m.Clinical.objects.create(**sec, signs_symptoms=''),
        characteristic_table=m.CharacteristicsTable.objects.create(
            table_identifier=name, table_title='', table_caption=''),
    )


@override_settings(CACHES=LOCMEM, SECURE_SSL_REDIRECT=False)
class RateLimitTests(TestCase):
    def setUp(self):
        cache.clear()

    def test_sixth_feedback_post_in_a_minute_is_blocked(self):
        codes = [self.client.post('/disease_search/?disease=hd', {}).status_code for _ in range(6)]
        self.assertNotIn(429, codes[:5])
        self.assertEqual(codes[5], 429)

    @override_settings(CACHES={'default': {'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
                                           'LOCATION': 'missing_cache_table'}})
    def test_missing_cache_table_does_not_break_feedback(self):
        with self.assertLogs('polyQ.request_limiter', level='ERROR'):
            response = self.client.post('/disease_search/?disease=hd', {})
        self.assertEqual(response.status_code, 302)  # normal form handling, not a 500

    def test_get_requests_are_not_limited(self):
        for _ in range(10):
            self.assertNotEqual(self.client.get('/disease_search/?disease=zzz').status_code, 429)


@override_settings(SECURE_SSL_REDIRECT=False)
class DiseaseSearchTests(TestCase):
    def test_recaptcha_widget_renders_as_html_with_nonce(self):
        from feedback.forms import FeedbackForm
        html = str(FeedbackForm(nonce='abc')['captcha'])
        self.assertIn('<script nonce="abc"', html)
        self.assertNotIn('&lt;script', html)

    def test_disease_page_recaptcha_script_carries_the_header_nonce(self):
        import re
        make_disease('HD')
        response = self.client.get('/disease_search/?disease=hd')
        self.assertEqual(response.status_code, 200)
        header = response['Content-Security-Policy']
        nonce = re.search(r"'nonce-([^']+)'", header).group(1)
        self.assertIn(f'<script nonce="{nonce}" type="text/javascript">', response.content.decode())

    def test_unknown_url_uses_custom_page_with_real_404_status(self):
        response = self.client.get('/no-such-page')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'not-found-page.html')
        self.assertContains(response, 'This page does not exist', status_code=404)

    def test_server_error_page_has_500_status_and_its_own_wording(self):
        from django.test import RequestFactory
        from polyQ.views import custom_error_view
        response = custom_error_view(RequestFactory().get('/'))
        self.assertEqual(response.status_code, 500)
        html = response.content.decode()
        self.assertIn('Something went wrong on our side', html)
        self.assertNotIn('does not exist', html)

    def test_new_outcome_replaces_old_one_in_redirect(self):
        # invalid (empty) form posted from a URL that still carries an old success flag
        response = self.client.post('/disease_search/?disease=hd&sent=mailTrue', {})
        self.assertEqual(response.status_code, 302)
        self.assertIn('error=true', response['Location'])
        self.assertNotIn('sent=', response['Location'])
        self.assertIn('disease=hd', response['Location'])

    def test_missing_or_unknown_disease_is_404_not_500(self):
        self.assertEqual(self.client.get('/disease_search/').status_code, 404)
        self.assertEqual(self.client.get('/disease_search/?disease=zzz').status_code, 404)


@override_settings(DEFAULT_FROM_EMAIL='sender@example.com', FEEDBACK_ADMIN_EMAIL='admin@example.com')
class NotificationEmailTests(TestCase):
    def test_admin_and_visitor_emails_use_addresses_from_settings(self):
        from django.core import mail
        from polyQ import views
        data = {'visitor_name': 'ana', 'subject': 's', 'message': 'm'}
        views.send_notification_emails(data, 'visitor@example.com')
        admin_mail, visitor_mail = mail.outbox
        self.assertEqual((admin_mail.from_email, admin_mail.to), ('sender@example.com', ['admin@example.com']))
        self.assertEqual((visitor_mail.from_email, visitor_mail.to), ('sender@example.com', ['visitor@example.com']))

    @override_settings(FEEDBACK_ADMIN_EMAIL=None)
    def test_missing_admin_address_is_logged_and_visitor_still_emailed(self):
        from django.core import mail
        from polyQ import views
        data = {'visitor_name': 'ana', 'subject': 's', 'message': 'm'}
        with self.assertLogs('polyQ.views', level='WARNING'):
            views.send_notification_emails(data, 'visitor@example.com')
        self.assertEqual([m.to for m in mail.outbox], [['visitor@example.com']])

    def test_no_visitor_email_when_address_blank(self):
        from polyQ import views
        data = {'visitor_name': 'ana', 'subject': 's', 'message': 'm'}
        with mock.patch.object(views, 'send_mail') as admin_mail, \
                mock.patch.object(views, 'EmailMessage') as visitor_mail:
            views.send_notification_emails(data, '')
        admin_mail.assert_called_once()
        visitor_mail.assert_not_called()

    def test_email_failure_is_logged_not_raised(self):
        from polyQ import views
        with mock.patch.object(views, 'send_mail', side_effect=OSError('smtp down')), \
                self.assertLogs('polyQ.views', level='ERROR'):
            views.send_notification_emails({'visitor_name': 'ana'}, '')
