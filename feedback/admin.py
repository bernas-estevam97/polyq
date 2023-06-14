from django.contrib import admin

from .models import Form

class FormAdmin(admin.ModelAdmin):
    list_display = ('visitor_name', 'email', 'subject', 'message', 'date',)
    list_filter = ('date',)
    search_fields = ('visitor_name', 'subject',)

    class Meta:
        model = Form


admin.site.register(Form, FormAdmin)
