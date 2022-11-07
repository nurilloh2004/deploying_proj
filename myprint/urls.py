from unicodedata import name
from django.urls import path
from .views import *

 
app_name = "myprint"

urlpatterns = [
    path('', home, name='home'),
    path('logout/', logoutview, name='logout'),
    path('parent/<int:pk>/', parent, name='parent'),
    path('parent_product/<int:pk>/', parent_product, name='parent_product'),
    path('contact/', contact, name='contact'),
    path('portfolio/', portfolio, name='portfolio'),
    path('design/', design, name='design'),
    path('printing_large/', printing_large, name='printing_large'),
    path('promotional_products/', promotional_products, name='promotional_products'),
    path('markirovka/', markirovka, name='markirovka'),
    path('printing_paper/', printing_paper,  name='printing_paper'),
    path('printing_textile/', printing_textile, name='printing_textile'),
    path('textile_products/', textile_products, name='textile_products'),
    path('advertisement/', aboutview, name='advertisement'),
    path('all/', Home.as_view(), name='all'),
    path('create/', createView, name="create"),
    path('list/', listView, name="list"),
    path('user_login_view/', user_login, name='login'),
    path('create-pdf/', generate_pdf, name="create_pdf"),
    path('aboutview/', aboutview, name='aboutview'),
    path('servicecategory/', servicecategory, name='servicecategory'),
]
