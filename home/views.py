from django.shortcuts import render
from .models import HeroSlider


def home(request):
    hero_slider = HeroSlider.objects.last()
    template = 'home/home.html'
    context = {
        'hero_slider': hero_slider
    }
    return render(request, template, context)
