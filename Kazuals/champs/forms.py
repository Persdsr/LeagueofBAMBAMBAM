from django import forms

from champs.models import Build
from service.models import Meme


class BuildForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'class': ''}))

    class Meta:
        model = Build
        exclude = ('slug', 'create_at', 'author', 'items')

class MemeForm(forms.ModelForm):
    file = forms.FileField(label='', widget=forms.FileInput(attrs={'id': 'fileInput'}))

    class Meta:
        model = Meme
        fields = ('file',)