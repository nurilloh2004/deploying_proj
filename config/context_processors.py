
from myprint.models import Category, Settings



def all_category(request):
    return {
        "allcategory": Category.objects.filter(parent=None).all(),
    }
