from general.models import sociallinks, copyright, dynAddress
from django.http import JsonResponse

def context_processor(request):
    social = sociallinks.objects.all()
    cpyright = copyright.objects.first()
    lonlat = dynAddress.objects.first()
    contextview = {
        'social': social,
        'cpyright': cpyright,
        'lonlat': lonlat,
    }

    return contextview