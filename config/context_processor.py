from deploying_proj.myprint.models import Settings
from myprint.models import Category, Settings



def all_category(request):
    return {
        "allcategory": Category.objects.filter(parent=None).all(),
        "phone": Settings.objects.get(key='phone').value,
    }
