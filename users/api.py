from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response

from users.models import Subscribers, SubLists
from users.serializers import SubscribersSerializer, DownloadListSerializer, SubListsSerializer
from users.service.services import ImportSubsFromList


class SubscribersListViewSet(viewsets.ReadOnlyModelViewSet):
    """Получение списка подписчиков"""
    queryset = Subscribers.objects.all().order_by('surname', 'name')
    serializer_class = SubscribersSerializer


class SubListsViewSet(viewsets.ReadOnlyModelViewSet):
    """Получение всех списков рассылок"""
    queryset = SubLists.objects.all()
    serializer_class = SubListsSerializer


class ListCreateViewSet(viewsets.ModelViewSet):
    """Загрузка списк рассылки из xlsx файла"""
    serializer_class = DownloadListSerializer

    def create(self, request, *args, **kwargs):
        serialize = self.serializer_class(data=request.data)
        if serialize.is_valid(raise_exception=True):
            lst = serialize.save()
            if ImportSubsFromList(lst.id, request.FILES['file']) is True:
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(data='Произошла ошибка при импорте списка подписчиков', status=status.HTTP_400_BAD_REQUEST)

        else:
            return JsonResponse({'error': serialize.errors})