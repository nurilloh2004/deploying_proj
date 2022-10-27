from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import OrderServiceForm


# def service_type(request, pk):
#     service = Type_Services.objects.filter(type_id=pk)
#     image = Image.objects.filter(type_sevice_id=pk)
#     form = OrderServiceForm()
#     if request.method == 'POST':
#         form = OrderServiceForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     context = {
#         'form': form,
#         'service': service,
#         'pk': pk,
#         'image': image,
#     }
#     return render(request, 'main/service_type.html', context=context)



# def handle_uploaded_file(f):
#     with open('some/file/name.txt', 'wb+') as destination:
#         for chunk in f.chunks():
#              destination.write(chunk)

def handle_upload_file(f):
    with open('media/forma/' + f.files , 'wb+') as destiantion:
        for chunk in f.chunks():
            destiantion.write(chunk)