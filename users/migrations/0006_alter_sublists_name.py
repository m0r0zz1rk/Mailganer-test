# Generated by Django 4.1.3 on 2022-11-16 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_sublists_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sublists',
            name='name',
            field=models.CharField(max_length=250, unique=True, verbose_name='Наименование списка рассылки'),
        ),
    ]
