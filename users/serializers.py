from rest_framework import serializers

from users.models import Subscribers, SubLists


class SubscribersSerializer(serializers.ModelSerializer):
    """Сериализация записей модели подписчиков"""

    class Meta:
        model = Subscribers
        fields = '__all__'


class SubListsSerializer(serializers.ModelSerializer):
    """Сериализаааия записей модели списка рассылок"""
    subscribers = SubscribersSerializer(many=True)

    class Meta:
        model = SubLists
        fields = '__all__'


class DownloadListSerializer(serializers.ModelSerializer):
    """Сериализация файла со списком рассылки"""

    class Meta:
        model = SubLists
        fields = ['name', 'file']