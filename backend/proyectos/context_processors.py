from django.utils.timezone import now

def global_context(request):
    return {
        'now': now(),
        'site_name': "Portafolio de José Miguel",
    }
