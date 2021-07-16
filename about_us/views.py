from django.shortcuts import render

from .models import AboutUs, Teams,TeamBanner


def about_us_page(request):
    about = AboutUs.objects.last()
    teams = Teams.objects.all()
    banner = TeamBanner.objects.last()


    context = {
        'about': about,
        'teams': teams,
        'banner': banner.get_banner,

    }
    return render(request, 'about/about_us.html', context)
