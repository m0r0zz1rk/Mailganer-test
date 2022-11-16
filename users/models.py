import datetime

from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models


class Subscribers(models.Model):
    """Модель подписчиков"""
    email = models.EmailField(
        max_length=200,
        unique=True,
        default='',
        null=False,
        verbose_name='Email'
    )
    name = models.CharField(
        max_length=75,
        blank=False,
        null=False,
        verbose_name='Имя'
    )
    surname = models.CharField(
        max_length=75,
        blank=False,
        null=False,
        verbose_name='Фамилия'
    )
    birthday = models.DateField(
        default=datetime.date.today,
        verbose_name='Дата рождения'
    )

    objects = models.Manager()

    def __str__(self):
        return f'{self.surname} {self.name} ({self.email})'

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'


class SubLists(models.Model):
    """Модель списков рассылки"""
    name = models.CharField(
        max_length=250,
        unique=True,
        blank=False,
        verbose_name='Наименование списка рассылки'
    )
    subscribers = models.ManyToManyField(
        Subscribers,
        verbose_name='Подписчики'
    )
    file = models.FileField(
        default=None,
        validators=[FileExtensionValidator(['xlsx',])],
        verbose_name='Файл со списком рассылки'
    )

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Список рассылки'
        verbose_name_plural = 'Списки рассылки'
# Create your models here.
