from django.contrib import admin

from mail.models import Mailings


@admin.register(Mailings)
class MailingsAdmin(admin.ModelAdmin):
    pass

# Register your models here.
