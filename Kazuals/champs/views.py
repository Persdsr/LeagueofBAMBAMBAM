import json

from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView

from champs.forms import BuildForm, MemeForm
from champs.models import Build
from champs.service.items_on_db import get_all_champs, get_all_items, get_champ_info
from service.models import Meme


def home_page(request):
    error = ''
    memes = Meme.objects.all()
    if request.method == 'POST':
        form = MemeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'нужно отправить видео'
    else:
        form = MemeForm()
    return render(request, 'main.html', {"memes": memes, 'form': form, 'error': error})


def champs_page(request):
    all_champs = get_all_champs()
    return render(request, 'champions.html', {'champs': all_champs})


class ChampsView(ListView):
    model = Build
    template_name = 'champions.html'
    context_object_name = 'builds'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['champs'] = get_all_champs()
        return context


class ChampionBuild(DetailView):
    model = Build
    template_name = 'guide.html'
    context_object_name = 'builds'
    slug_url_kwarg = 'guide_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['champ'] = get_champ_info(self.kwargs['champion_id'])
        items_raw = Build.objects.get(title__iexact=self.kwargs['guide_slug'].lower())
        items_json = json.loads(items_raw.items)
        items = []
        for key, value in items_json.items():
            items.append({
                'name': key,
                'image': value
            })
        context['items'] = items
        return context


def champion_info(request, champion_slug):
    recommended_builds = Build.objects.order_by('-id')[:3]
    champ_info = get_champ_info(champion_slug)
    return render(request, 'champion_info.html', {'champion': champ_info})


class CreateBuild(CreateView):
    model = Build
    template_name = 'create_build.html'
    form_class = BuildForm
    slug_url_kwarg = 'home'
    success_url = 'champs'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = get_all_items()
        para = Build.objects.get(title='NEW STE')
        b = json.loads(para.items)
        return context

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        form.instance.author = self.request.user

        my_array = self.request.POST.get('my_array')
        t_array = my_array.replace("'", '"')
        form.instance.items = t_array

        return super().form_valid(form)
