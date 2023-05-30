from django.core.validators import FileExtensionValidator
from django.db import models


class Meme(models.Model):
    file = models.FileField(verbose_name='Файл с мемом', validators=[FileExtensionValidator(['mp4'])])
    create_at = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
