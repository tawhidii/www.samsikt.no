from .models import TopBarSettings


def top_bar_values(request):
    top_bar = TopBarSettings.objects.first()
    context = {
        'top_bar': top_bar
    }
    return context
