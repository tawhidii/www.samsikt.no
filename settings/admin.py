from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import FooterSettings, TopBarSettings


class FooterSettingsAdmin(SummernoteModelAdmin):
    summernote_fields = ('footer_short_about','footer_contact_details',)


admin.site.register(FooterSettings, FooterSettingsAdmin)
admin.site.register(TopBarSettings)
