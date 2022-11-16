from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view

from templates.models import MailingTemplates
from templates.serializers import MailingTemplatesSerializer
from users.models import Subscribers


class TemplatesListViewSet(viewsets.ReadOnlyModelViewSet):
    """Получение списка всех макетов рассылки"""
    queryset = MailingTemplates.objects.all().order_by('name')
    serializer_class = MailingTemplatesSerializer


class TemplateCreateViewSet(viewsets.ModelViewSet):
    """Добавление нового макета рассылки"""
    queryset = MailingTemplates.objects.all()
    serializer_class = MailingTemplatesSerializer


@api_view(['GET'])
def check(request):
    sub = Subscribers.objects.all().latest('id')
    field_object = Subscribers._meta.get_field('birthday')
    field_value = field_object.value_from_object(sub)
    str_birthday = field_value.strftime('%d.%m.%Y')
    #str_bithday = f'{field_value[8:]}.{field_value[5:7]}.{field_value[:4]}'
    return JsonResponse({'birthday': str_birthday})

