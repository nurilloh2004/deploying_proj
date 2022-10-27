from cgitb import html
from django.shortcuts import render, redirect
from django.views.generic import (TemplateView, ListView, CreateView, DetailView, FormView)
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
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




def home(request):
    categories = Category.objects.filter(parent=None)
    products = Product.objects.all()
    servistype = TypeService.objects.all()
    menuservice = MenuService.objects.all()
    sponsor = Sponsors.objects.all()
    menutarif = MenuTariff.objects.all()
    tarif = Tariff.objects.all()
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
        'menutarif': menutarif,
        'tarif': tarif,
        'categories': categories,
        'products': products,
    }
    return render(request, 'main/index.html', context=context)
    

def contact(request):
    return render(request, 'main/contact.html')

def portfolio(request):
    image = Portfolio.objects.all()
    context = {
        "image": image
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


 #🔻 🔻 🔻 🔻 🔻 🔻 🔻 🔻 🔻 🔻 🔻 🔻 
 #🔻 🔻


@csrf_exempt
def printing_large(request):
    form = OrderServiceForm()
    sub = SubLargeFormat.objects.all()
    lar = LargeFormat.objects.all()
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
        print("<-----------------------__>>>>", request.POST)
        if form.is_valid():
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
def poligraphy_product(request, pk):
    product = Product.objects.filter(category_id=pk)
    form = OrderServiceForm()
    if request.method == 'POST':
        form = OrderServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "product": product,
        'pk': pk,
        'form' : form
    }
    return render(request, 'main/poligraphy-products.html', context=context)


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



# def listView(request):
#     order = OrderForm.objects.filter(amount='amount', price='price',VAT='VAT')
#     total = 0
#     all_price = order.price * order.amount
#     percent_sum = (all_price / 100) * order.VAT
#     sum_list = all_price + percent_sum
#     total = total + sum_list
#     context = {}

#     context['order'] = order
#     context['sum_list'] = sum_list
#     context['all_price'] = all_price
#     context['total'] = total
#     if order.VAT:
#         total = total + (total*order.VAT/100)
#         context['total_sum']=total
#     else:
#         context = {}
#     return render(request, 'invoice.html', context=context)



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


# def pdf_report_create(request):
#     order = OrderForm.objects.all()

#     template_path = 'pdf_convert/pdfReport.html'

#     context = {'order': order}

#     response = HttpResponse(content_type='application/pdf')

#     response['Content-Disposition'] = 'filename="orders_report.pdf"'

#     template = get_template(template_path)

#     html = template.render(context)

#     # create a pdf
#     pisa_status = pisa.CreatePDF(
#        html, dest=response)
#     # if error then show some funy view
#     if pisa_status.err:
#        return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response


# import os
# from django.conf import settings
# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa
# from django.contrib.staticfiles import finders
# from config import settings

# def link_callback(uri, rel):
#         """
#         Convert HTML URIs to absolute system paths so xhtml2pdf can access those
#         resources
#         """
#         result = finders.find(uri)
#         if result:
#                 if not isinstance(result, (list, tuple)):
#                         result = [result]
#                 result = list(os.path.realpath(path) for path in result)
#                 path=result[0]
#         else:
#                 sUrl = settings.STATIC_URL        # Typically /static/
#                 sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
#                 mUrl = settings.MEDIA_URL         # Typically /media/
#                 mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/
#                 if uri.startswith(mUrl):
#                         path = os.path.join(mRoot, uri.replace(mUrl, ""))
#                 elif uri.startswith(sUrl):
#                         path = os.path.join(sRoot, uri.replace(sUrl, ""))
#                 else:
#                         return uri
#         # make sure that file exists
#         if not os.path.isfile(path):
#                 raise Exception(
#                         'media URI must start with %s or %s' % (sUrl, mUrl)
#                 )
#         return path

# def render_pdf_view(request):
#     template_path = 'multi_forms/list.html'
#     context = {'myvar': 'this is your template context'}
#     # Create a Django response object, and specify content_type as pdf
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="report.pdf"'
#     # find the template and render it.
#     template = get_template(template_path)
#     html = template.render(context)

#     # create a pdf
#     pisa_status = pisa.CreatePDF(
#        html, dest=response, link_callback=link_callback)
#     # if error then show some funny view
#     if pisa_status.err:
#        return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response




def not_found_page(request, exception):
    return render(request, 'main.not_found.html')

#Rendering html page to pdf


from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("cp1252")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


data = {
	"company": "Dennnis Ivanov Company",
	"address": "123 Street name",
	"city": "Vancouver",
	"state": "WA",
	"zipcode": "98663",


	"phone": "555-555-2345",
	"email": "youremail@dennisivy.com",
	"website": "dennisivy.com",
	}

#Opens up page as PDF
class ViewPDF(View):
	def get(self, request, *args, **kwargs):

		pdf = render_to_pdf('pdf_convert/pdfReport.html', data)
		return HttpResponse(pdf, content_type='application/pdf')


def typeimage(request, pk):
    t_image = Image.objects.filter(type_sevice_id=pk)
    context = {
        't_image': t_image
    }
    return render(request, 'main/reklama_image.html', context=context)