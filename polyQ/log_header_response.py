import logging

logger = logging.getLogger('django.request')

class LogResponseHeadersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        csp = response.get('Content-Security-Policy')
        if csp:
            logger.info(f"CSP header set: {csp}")
        else:
            logger.warning("No CSP header found on response")
        return response
