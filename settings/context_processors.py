from .models import TopBarSettings,FooterSettings


def top_bar_values(request):
    top_bar = TopBarSettings.objects.last()
    context = {
        'top_bar': top_bar
    }
    return context


def footer_values(request):
    footer = FooterSettings.objects.last()
    context = {
        'footer': footer
    }
    return context