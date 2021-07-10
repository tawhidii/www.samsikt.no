from django.contrib import admin

from .models import FooterSettings,TopBarSettings

admin.site.register(FooterSettings)
admin.site.register(TopBarSettings)