from django.contrib import admin

from users.models import Subscribers, SubLists


@admin.register(Subscribers)
class SubscribersAdmin(admin.ModelAdmin):
    pass


@admin.register(SubLists)
class SubListsAdmin(admin.ModelAdmin):
    pass
# Register your models here.
