# Generated by Django 4.1.3 on 2022-11-16 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_subscribers_email'),
        ('mail', '0002_mailings_complete'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackingJournal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_open', models.DateTimeField(auto_now_add=True, verbose_name='Время просмотра письма')),
                ('mailing', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='mail.mailings', verbose_name='Рассылка')),
                ('sub', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.subscribers', verbose_name='Подписчик')),
            ],
            options={
                'verbose_name': 'Запись о просмотре письма',
                'verbose_name_plural': 'Записи о просмотре писем',
            },
        ),
    ]
