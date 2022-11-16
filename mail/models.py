import datetime

from django.db import models

from templates.models import MailingTemplates
from users.models import SubLists, Subscribers


class Mailings(models.Model):
    """Модель рассылок"""
    name = models.CharField(
        max_length=150,
        verbose_name='Название рассылки'
    )
    sublist = models.ForeignKey(
        SubLists,
        on_delete=models.PROTECT,
        default=None,
        blank=False,
        verbose_name='Список рассылки'
    )
    template = models.ForeignKey(
        MailingTemplates,
        on_delete=models.PROTECT,
        default=None,
        blank=False,
        verbose_name='Макет письма рассылки'
    )
    now = models.BooleanField(
        default=True,
        verbose_name='Рассылка писем сейчас'
    )
    time_mail = models.DateTimeField(
        default=datetime.datetime.now,
        verbose_name='Дата и время рассылки писем'
    )
    complete = models.BooleanField(
        default=False,
        verbose_name='Завершено'
    )

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class TrackingJournal(models.Model):
    """Журнал просмотренных писем"""
    mailing = models.ForeignKey(
        Mailings,
        on_delete=models.PROTECT,
        default=None,
        blank=False,
        verbose_name='Рассылка'
    )
    sub = models.ForeignKey(
        Subscribers,
        on_delete=models.CASCADE,
        default=None,
        blank=False,
        verbose_name='Подписчик'
    )
    time_open = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время просмотра письма'
    )

    objects = models.Manager()

    def __str__(self):
        return f'{self.mailing.name} : {self.sub.email}'

    class Meta:
        verbose_name = 'Запись о просмотре письма'
        verbose_name_plural = 'Записи о просмотре писем'



