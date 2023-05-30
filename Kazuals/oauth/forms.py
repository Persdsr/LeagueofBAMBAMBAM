from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms

from oauth.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'forms__username', 'placeholder': "Введите имя пользователя"}))
    lol_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'forms__username', 'placeholder': "Введите имя призывателя"}))
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'class': 'forms__username', 'placeholder': "Введите почту"}))
    bio = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'forms__username', 'placeholder': "О себе"}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'forms__username', 'placeholder': "Введите пароль"}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'forms__username', 'placeholder': "Подтверждение пароля"}))

    class Meta:
        model = CustomUser
        fields = ('username', 'lol_name', 'gender', 'bio', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'lol_name', 'gender', 'bio', 'email')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'forms__username', 'placeholder': "Введите имя пользователя"}))
    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'forms__username', 'placeholder': "Введите пароль"}))

    class Meta:
        model = CustomUser
        fields = ('username', 'password')