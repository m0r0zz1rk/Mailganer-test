from rest_framework import serializers

from templates.models import MailingTemplates


class MailingTemplatesSerializer(serializers.ModelSerializer):
    """Сериализация макетов рассылки"""
    class Meta:
        model = MailingTemplates
        fields = '__all__'