from django.urls import path

from users.api import SubscribersListViewSet, ListCreateViewSet, SubListsViewSet

urlpatterns = [
    path('subscribers/', SubscribersListViewSet.as_view({'get': 'list'})),

    path('sub_lists/', SubListsViewSet.as_view({'get': 'list'})),

    path('download_list/', ListCreateViewSet.as_view({'post': 'create'})),
]