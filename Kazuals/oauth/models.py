from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models


class CustomUser(AbstractUser):
    """Модель кастомного юзера"""
    GENDERS = (
        ('m', 'Мужчина'),
        ('f', 'Посудомойка'),
    )

    bio = models.TextField('О себе', max_length=2000, blank=True, null=True)
    lol_name = models.CharField('Имя призывателя', max_length=15, blank=True, null=True)
    avatar = models.ImageField(
        'Аватарка',
        upload_to='users_avatar/',
        blank=True, null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])])
    gender = models.CharField('Пол', max_length=1, choices=GENDERS, default='m')
