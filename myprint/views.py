from multiprocessing import context
from django.shortcuts import render, redirect
from django.views.generic import (TemplateView, ListView, CreateView, DetailView, FormView)
from django.contrib import messages
from django.urls import reverse
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView
from django.forms import modelformset_factory
from django.db import transaction, IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as auth_login
from django.contrib.auth import  authenticate
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, redirect
from django.views.generic import (TemplateView, ListView, CreateView, DetailView, FormView)
from django.contrib import messages
from django.urls import reverse
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView
from django.forms import modelformset_factory
from django.db import transaction, IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import  authenticate
from django.contrib.auth import login as auth_login




def home(request):
    servistype = TypeService.objects.all()
    menuservice = MenuService.objects.all()
    print("Menyu------------>>>>>>>>", menuservice)

    form = OrForm()
    if request.method == 'POST':
        form = OrForm(request.POST)
        print("<-----------------------__>>>>", request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = OrForm()
    context = {
        "servistype": servistype,
        "menuservice": menuservice,
        'form' : form
    }
    return render(request, 'main/index.html', context=context)
    

def contact(request):
    return render(request, 'main/contact.html')

def portfolio(request):
    image = AboutImage.objects.all()
    context = {
        "image": image
    }
    return render(request, 'main/portfolio.html', context=context)

def gift_product(request):
    return render(request, 'main/gifts-products.html')

def design(request):
    return render(request, 'main/dizayn.html')

def printing_large(request):
    form = OrForm()
    if request.method == 'POST':
        form = OrForm(request.POST)
        print("<-----------------------__>>>>", request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = OrForm()
    context = {
        'form' : form
    }
    return render(request, 'main/printing-largeformat.html' , context=context)

def promotional_products(request):
    return render(request, 'main/promotional-products.html')

def markirovka(request):
    form = OrForm()
    if request.method == 'POST':
        form = OrForm(request.POST)
        print("<-----------------------__>>>>", request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = OrForm()
    context = {
        'form' : form
    }
    return render(request, 'main/markirovka.html', context=context)
def poligraphy_product(request, pk):
    product = Product.objects.filter(category_id=pk)
    # categories = Category.objects.filter(parent=None).all()
    # children = Category.objects.filter(parent_id__in=[k.id for k in categories]).all()
    context = {
        "product": product,
        'pk': pk
        # "children": children
    }
    return render(request, 'main/poligraphy-products.html', context=context)

def printing_paper(request):
    form = OrForm()
    if request.method == 'POST':
        form = OrForm(request.POST)
        print("<-----------------------__>>>>", request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = OrForm()
    context = {
        'form' : form
    }
    return render(request, 'main/printing-paper.html' , context=context)

def printing_textile(request):
    form = OrForm()
    if request.method == 'POST':
        form = OrForm(request.POST)
        print("<-----------------------__>>>>", request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = OrForm()
    context = {
        'form' : form
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

# def get_name(request):
#     if request.method == 'POST':
#         form = OrderMForm(request.POST)
#         if form.is_valid():
            
#             return HttpResponseRedirect('/thanks/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()

#     return render(request, 'name.html', {'form': form})




# @csrf_exempt
# def test_form(request):
#     form = OrderMForm()
#     if request.method == 'POST':
#         form = OrderMForm(request.POST)
#         if form.is_valid():
#             form.save()
#     context = {"form": form}
#     return render(request, "main/testform.html", context)


# @csrf_exempt
# def test_form(request):
#     detail = OrderForm.objects.all()
#     form = OrderMForm()
#     if request.method == 'POST':
#         form = OrderMForm(request.POST)
#         if form.is_valid():
#             form.save()
#     context = {"form": form,
#                 "detail": detail
#                     }
#     return render(request, "main/application_order.html", context)




# def order(request):
#     if request.method == "POST":
#         form = OrderMForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'Reddit_app/order_thankyou.html')
#     else:
#         form = OrderMForm()
#     return render(request, 'Reddit_app/order_from_post.html', {"form": form})


@csrf_exempt
@login_required(login_url='login')
def listView(request):
    if request.user.is_authenticated:
        if OrderForm.objects.filter(manager=request.user.id):
            orders = OrderForm.objects.filter(manager=request.user.id).order_by('-id').first()
            total = 0
            all_price = orders.price * orders.amount
            percent_sum = (all_price / 100) * orders.VAT
            sum_list = all_price + percent_sum
            total = total + sum_list
            context = {}

            context['orders'] = orders
            context['sum_list'] = sum_list
            context['all_price'] = all_price
            context['total'] = total
            if orders.VAT:
                total = total + (total*orders.percent/100)
                context['total_sum']=total
        else:
            context = {}
        return render(request, 'invoice.html', context=context)



@csrf_exempt
def createView(request):
    context = {}
    print("ppppp -------------->>>>>", request.POST)
    OrdersFormset = modelformset_factory(OrderForm, form=OrdersForm)
    print("order form set", OrdersFormset)
    form = CustomerForm(request.POST or None)
    
    formset = OrdersFormset(request.POST or None, queryset=OrderForm.objects.none(), prefix='orders')
    
    if request.method == "POST":
        if form.is_valid() and formset.is_valid():
            print("print POST-------------->>>>", request.POST)
            try:
                with transaction.atomic():
                    student = form.save(commit=False)
                    student.save()

                    for order in formset:
                        data = order.save(commit=False)
                        data.student = student
                        print("print POST-------------->>>>", data)
                        data.save()
            except IntegrityError:
                print("Error encountered")
            
            return redirect('myprint:list')
    context['form'] = form
    context['formset'] = formset
    return render(request, 'multi_forms/create.html', context=context)

def list(request):
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


def pdf_report_create(request):
    order = OrderForm.objects.all()

    template_path = 'pdf_convert/pdfReport.html'

    context = {'order': order}

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="orders_report.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


