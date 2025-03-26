from django.contrib import admin

from .models import Form, Cache

@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ('visitor_name', 'email', 'subject', 'message', 'date',)
    list_filter = ('date',)
    search_fields = ('visitor_name', 'subject',)

    class Meta:
        model = Form


@admin.register(Cache)
class CacheAdmin(admin.ModelAdmin):
    list_display = ('key', 'expire_time')
    search_fields = ('key',)
    list_filter = ('expire_time',)



