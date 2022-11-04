from cgitb import html
from django.shortcuts import render, redirect
from django.views.generic import (TemplateView, ListView, CreateView, DetailView, FormView)
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.db import transaction, IntegrityError
from django.contrib.auth import  authenticate
from multiprocessing import context
from unicodedata import name
from django.views.generic.detail import SingleObjectMixin
from .models import *
from .forms import *
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import TemplateView, CreateView
from django.forms import modelformset_factory
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as auth_login
from .help_views import handle_upload_file




def home(request):
    # categories = Category.objects.filter(parent=None)
    products = Product.objects.all()
    servistype = TypeService.objects.all()
    menuservice = MenuService.objects.all()
    sponsor = Sponsors.objects.all()
    # menutarif = MenuTariff.objects.all()
    # tarif = Tariff.objects.all()
    form = OrderServiceForm()
    if request.method == 'POST':
        form = OrderServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
        "servistype": servistype,
        "menuservice": menuservice,
        'sponsor': sponsor,
        'products' : products
    }
    return render(request, 'main/index.html', context=context)
    

def contact(request):
    return render(request, 'main/contact.html') 

def portfolio(request):
    image = Portfolio.objects.all()
    product = Product.objects.all()
    context = {
        "image": image,
        'product': product
    }
    return render(request, 'main/portfolio.html', context=context)

def gift_product(request):
    return render(request, 'main/gifts-products.html')

def design(request):
    desig = Design.objects.filter()
    image = Image2.objects.filter()
    context = {
        'desig': desig,
        'image': image
    }
    return render(request, 'main/dizayn.html', context=context)

# def service_type(request, pk):
#     service = Type_Services.objects.filter(type_id=pk)
#     image = Image.objects.filter(type_sevice_id=pk)
#     context = {
#         'service': service,
#         'pk': pk,
#         'image': image
#     }
#     return render(request, 'main/service_type.html', context=context)

@csrf_exempt
def printing_large(request):
    form = OrderServiceForm()
    sub = SubLargeFormat.objects.all()
    lar = LargeFormat.objects.all()
    if request.method == 'POST':
        form = OrderServiceForm(request.POST, request.FILES)
        if form.is_valid():
            handle_upload_file(request.FILES['files'])
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/')
        else:
            form = OrderServiceForm()
    context = {
        'form' : form,
        'sub': sub,
        'lar': lar,
    }
    return render(request, 'main/printing-largeformat.html' , context=context)

def promotional_products(request):
    return render(request, 'main/promotional-products.html')
@csrf_exempt
def markirovka(request):
    laser = LaserPrint.objects.all()
    sub = SubLaserPrint.objects.all()
    image = Image2.objects.filter()
    form = OrderServiceForm()
    if request.method == 'POST':
        form = OrderServiceForm(request.POST, request.FILES)
        if form.is_valid():
            print("<<<<<<<<<<<<<<<<<<<", request.FILES)
            form.save()
            return redirect('/')
        else:
            form = OrderServiceForm()
    context = {
        'form' : form,
        'laser': laser,
        'image': image,
        'sub': sub
    }
    return render(request, 'main/markirovka.html', context=context)


def parent(request, pk):
    products = Product.objects.filter(category_id=pk)
    subcategory = SubCategory.objects.filter(category_id=pk)
    form = OrderServiceForm()
    if request.method == 'POST':
        form = OrderServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
        'subcategory': subcategory,
        'products': products
    }
    return render(request, 'main/poligraphy-products.html', context=context)


def parent_product(request, pk):
    product = SubCategory.objects.all()
    products = Product.objects.filter(subcategory_id=pk)
    subcategory = SubCategory.objects.filter(category_id=pk)
    form = OrderServiceForm()
    if request.method == 'POST':
        form = OrderServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
        'subcategory': subcategory,
        'products': products,
        'product': product,
    }
    return render(request, 'main/gifts-products.html', context=context)




@csrf_exempt
def printing_paper(request):
    dgprint = DigitalPrint.objects.all()
    sub = SubDigitalPrint.objects.all()
    image = Image2.objects.filter()
    form = OrderServiceForm()
    if request.method == 'POST':
        form = OrderServiceForm(request.POST, request.FILES)
        print("<-----------------------__>>>>", request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = OrderServiceForm()
    context = {
        'form' : form,
        'dgprint': dgprint,
        'image': image,
        'sub': sub,
    }
    return render(request, 'main/printing-paper.html' , context=context)


@csrf_exempt
def printing_textile(request):
    text = TextPrint.objects.all()
    subb = SUbTextPrint.objects.all()
    image = Image2.objects.filter()
    form = OrderServiceForm()
    if request.method == 'POST':
        form = OrderServiceForm(request.POST, request.FILES)
        print("<-----------------------__>>>>", request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = OrderServiceForm()
    context = {
        'form' : form,
        'image': image,
        'text' : text,
        'subb': subb,
    }
    return render(request, 'main/printing-textile.html', context=context)

def textile_products(request):
    return render(request, 'main/textile-products.html')

def advertisement(request):
    return render(request, 'main/about.html')

def invoice(request):
    return render(request, 'main/invoice.html')

def aboutview(request):
    about = About.objects.all()
    image = AboutImage.objects.all()
    context = {
        "about": about,
        "image": image
    }
    return render(request, 'main/about.html', context=context)


def servicecategory(request):
    page_service = MenuService.objects.all()
    context = {
        "page_service": page_service
    }
    return render(request, 'main/service_page.html', context=context)


class OrderCreateView(CreateView):
    queryset = OrderForm()
    template_name = 'application_order.html'
    fields = '__all__'
    success_url = '/application_order'




@csrf_exempt
def createView(request):
    context = {}
    OrdersFormset = modelformset_factory(OrderForm, form=OrdersForm)
    form = CustomerForm(request.POST or None)
    
    formset = OrdersFormset(request.POST or None, queryset=OrderForm.objects.none(), prefix='orders')
    
    if request.method == "POST":
        if form.is_valid() and formset.is_valid():
            try:
                with transaction.atomic():
                    student = form.save(commit=False)
                    student.save()

                    for order in formset:
                        data = order.save(commit=False)
                        data.student = student
                        data.save()
            except IntegrityError:
                print("Error encountered")
            
            return redirect('myprint:list')
    context['form'] = form
    context['formset'] = formset
    return render(request, 'multi_forms/create.html', context=context)






def listView(request):
    datas = OrderForm.objects.all()
    context = {'datas' : datas}
    return render(request, 'multi_forms/list.html', context=context)














class Home(TemplateView):
    template_name = 'all.html'


@csrf_exempt
def user_login(request):
    if request.method == 'GET':
        print("GET ---------------> ")
        form = UserLoginForm()
        context={'form': form}
        print(context)
        return render(request, template_name='main/login.html', context=context)
    else:
        form = UserLoginForm(request.POST)
        
        if form.is_valid():
            
            user_name = request.POST['phone_number']
            password = request.POST['password']

            print("phone   ", user_name)
            print("password --> ", password)
            user = User.objects.filter(phone_number=user_name).first()

            user = authenticate(phone_number=user_name, password=password)
            print("user --- ", user)
            if user:    
                auth_login(request, user)
                print("login ---> ", auth_login)
                return  render(request, 'main/success.html')
            else:
                return render(request, template_name='main/error.html', context={'login': auth_login})




def not_found_page(request, exception):
    return render(request, 'main.not_found.html')

from django.http import HttpResponse
from django.shortcuts import render

from .utils import *

def generate_pdf(request):
    datas = OrderForm.objects.all()
    context = {'datas': datas}
    pdf = html_to_pdf('pdf_convert/pdfReport.html', context=context)
    return HttpResponse(pdf, content_type='application/pdf')
