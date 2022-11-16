from django.contrib import admin

from templates.models import MailingTemplates


@admin.register(MailingTemplates)
class MailingTemplatesAdmin(admin.ModelAdmin):
    pass
# Register your models here.
