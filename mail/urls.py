from django.urls import path

from mail.api import MalingsListViewSet, MailingCreateViewSet, TrackingJournalViewSet

urlpatterns = [
    path('mailings/', MalingsListViewSet.as_view({'get': 'list'})),

    path('new_mailing/', MailingCreateViewSet.as_view({'post': 'create'})),

    path('journal/', TrackingJournalViewSet.as_view({'get': 'list'}))
]