from .models import Storesetting


def store_data(request):
    data = {
        'storeData': Storesetting.objects.first()
    }

    return data
