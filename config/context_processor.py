from myprint.models import Category



def all_category(request):
    return {
        "allcategory": Category.objects.filter(parent=None).all(),
        # "childrin": Category.objects.filter()
    }
