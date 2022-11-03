

from myprint.models import Category, Settings, Type



def all_category(request):
    return {
        "allcategory": Category.objects.filter(),
        # "phone":Settings.objects.get(key='phone').value,
        # "instagram":Settings.objects.get(key='instagram').value,
        # "facebook":Settings.objects.get(key='facebook').value,
        # "telegram":Settings.objects.get(key='telegram').value,
        # "work_info1":Settings.objects.get(key='work_info1').value,
        # "work_info2":Settings.objects.get(key='work_info2').value,
        # "location1":Settings.objects.get(key='location1').value,
        # "location2":Settings.objects.get(key='location2').value,
        # # "servicecategory": Type.objects.all(),
        # "description": Settings.objects.get(key='description').value,
    }
 