# Generated by Django 4.1.2 on 2023-05-09 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('champs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='items',
            field=models.TextField(default='[]', verbose_name='Предметы'),
        ),
    ]
