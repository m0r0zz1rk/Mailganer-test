import os

from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response

from mail.celery.tasks import ActualMailing

from mail.models import Mailings, TrackingJournal
from mail.serializers import MailingSerializer, MailingCreateSerializer, TrackingJournalSerializer


class MalingsListViewSet(viewsets.ReadOnlyModelViewSet):
    """Получение списка всех рассылок"""
    queryset = Mailings.objects.all().order_by('id')
    serializer_class = MailingSerializer


class MailingCreateViewSet(viewsets.ModelViewSet):
    """Создание новой рассылки"""
    queryset = Mailings.objects.all()
    serializer_class = MailingCreateSerializer

    def create(self, request, *args, **kwargs):
        serialize = self.serializer_class(data=request.data)
        if serialize.is_valid(raise_exception=True):
            mailing = serialize.save()
            if 'now' in request.data:
                ActualMailing.delay(mailing.id)
            return Response(status=status.HTTP_200_OK)
        else:
            return JsonResponse({'error': serialize.errors})


class TrackingJournalViewSet(viewsets.ReadOnlyModelViewSet):
    """Просмотр журнала открытия писем"""
    queryset = TrackingJournal.objects.all().order_by('-time_open')
    serializer_class = TrackingJournalSerializer


class PixelViewSet(viewsets.ViewSet):
    """Отслеживание открытия письма"""
    def AddOpenMail(self, request, *args, **kwargs):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_data = open(os.path.join(script_dir, 'pixel/1x1.png'), 'rb').read()
        mailing = Mailings.objects.get(id=kwargs.get('id'))
        data = {
            'mailing': mailing.name,
            'sub': kwargs.get('email')
        }
        serialize = TrackingJournalSerializer(data=data)
        if serialize.is_valid(raise_exception=True):
            serialize.save()
        return HttpResponse(image_data, content_type="image/png")
