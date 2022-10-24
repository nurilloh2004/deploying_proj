

from myprint.models import Category, Settings, Type



def all_category(request):
    return {
        "allcategory": Category.objects.filter(parent=None).all(),
        "phone":Settings.objects.get(key='phone').value,
        "instagram":Settings.objects.get(key='instagram').value,
        "facebook":Settings.objects.get(key='facebook').value,
        "telegram":Settings.objects.get(key='telegram').value,
        "work_info":Settings.objects.get(key='work_info').value,
        "location1":Settings.objects.get(key='location1').value,
        "location2":Settings.objects.get(key='location2').value,
        "servicecategory": Type.objects.all(),
    }
 