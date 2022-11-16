from rest_framework import serializers

from mail.models import Mailings, TrackingJournal
from templates.models import MailingTemplates
from users.models import SubLists, Subscribers


class MailingSerializer(serializers.ModelSerializer):
    """Сериализация рассылок"""
    sublist = serializers.SlugRelatedField(slug_field='name', queryset=SubLists.objects.all().order_by('name'))
    template = serializers.SlugRelatedField(slug_field='name', queryset=MailingTemplates.objects.all().order_by('name'))

    class Meta:
        model = Mailings
        fields = '__all__'


class MailingCreateSerializer(serializers.ModelSerializer):
    """Сериализация рассылок"""
    sublist = serializers.SlugRelatedField(slug_field='name', queryset=SubLists.objects.all().order_by('name'))
    template = serializers.SlugRelatedField(slug_field='name', queryset=MailingTemplates.objects.all().order_by('name'))

    class Meta:
        model = Mailings
        exclude = ('complete',)


class TrackingJournalSerializer(serializers.ModelSerializer):
    """Сериализация журнала просмотра писем"""
    mailing = serializers.SlugRelatedField(slug_field='name', queryset=Mailings.objects.all())
    sub = serializers.SlugRelatedField(slug_field='email', queryset=Subscribers.objects.all())

    class Meta:
        model = TrackingJournal
        fields = '__all__'
