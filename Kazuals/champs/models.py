import json

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse

from oauth.models import CustomUser


class Build(models.Model):
    title = models.CharField(verbose_name='Название', max_length=20)
    author = models.ForeignKey(CustomUser, verbose_name='Автор', on_delete=models.CASCADE, related_name='build_author')
    champion = models.CharField(verbose_name='Чемпион', max_length=12)
    create_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    items = models.TextField(verbose_name='Предметы', default='[]')
    slug = models.SlugField(verbose_name='url', unique=True)


    def get_absolute_url(self):
        return reverse('detail_guide', kwargs={'guide_slug': self.slug, 'champion_id': self.champion})

    def __str__(self):
        return self.title
