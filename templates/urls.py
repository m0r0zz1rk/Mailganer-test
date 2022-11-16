from django.urls import path

from templates.api import TemplatesListViewSet, TemplateCreateViewSet, check

urlpatterns = [
    path('templates/', TemplatesListViewSet.as_view({'get': 'list'})),
    path('new_template/', TemplateCreateViewSet.as_view({'post': 'create'})),
    path('check/', check),
]