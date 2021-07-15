from django.shortcuts import render

from .models import AboutUs


def about_us_page(request):
    about = AboutUs.objects.last()
    print(about)
    context = {
        'about': about
    }
    return render(request, 'about/about_us.html', context)
