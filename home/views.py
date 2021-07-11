from django.shortcuts import render
from .models import(
    HeroSlider,
    Services
)


def home(request):
    hero_slider = HeroSlider.objects.last()
    home_services = Services.objects.all()
    template = 'home/home.html'
    context = {
        'hero_slider': hero_slider,
        'home_services': home_services
    }
    return render(request, template, context)
