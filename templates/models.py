from django.db import models


class MailingTemplates(models.Model):
    """Модель макетов рассылки"""
    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Наименование макета'
    )
    html = models.TextField(
        max_length=100000,
        verbose_name='Код макета'
    )

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Макет рассылки'
        verbose_name_plural = 'Макеты рассылки'
# Create your models here.
