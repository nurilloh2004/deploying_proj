from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import OrderServiceForm

def handle_upload_file(f):
    with open('media/forma/' + f.files , 'wb+') as destiantion:
        for chunk in f.chunks():
            destiantion.write(chunk)