# from django.views.generic.base import TemplateView
#
#
# class HomeView(TemplateView):
#     template_name = 'home/home.html'
#
from django.shortcuts import render


def home(request):
    template = 'home/home.html'
    context = {}
    return render(request,template,context)
