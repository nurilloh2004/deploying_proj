

from myprint.models import Category, Settings, CEO



def all_category(request):
    return {
        "allcategory": Category.objects.filter(parent=None).all(),
        "phone":Settings.objects.get(key='phone').value,
        "instagram":Settings.objects.get(key='instagram').value,
        "facebook":Settings.objects.get(key='facebook').value,
        "telegram":Settings.objects.get(key='telegram').value,
        "Logo":Settings.objects.get(key='Logo').logo,
    }
 