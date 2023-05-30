# Generated by Django 4.1.2 on 2023-05-09 18:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0003_alter_customuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='users_avatar/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png'])], verbose_name='Аватарка'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='bio',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='О себе'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='lol_name',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Имя призывателя'),
        ),
    ]