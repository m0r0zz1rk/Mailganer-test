# Generated by Django 4.1.3 on 2022-11-16 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0002_alter_mailingtemplates_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailingtemplates',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Наименование макета'),
        ),
    ]
