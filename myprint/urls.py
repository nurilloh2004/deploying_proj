from unicodedata import name
from django.urls import path
from .views import *
from .help_views import *
 
app_name = "myprint"

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('portfolio/', portfolio, name='portfolio'),
    path('gift_product/', gift_product, name='gift_product'),
    path('design/', design, name='design'),
    path('printing_large/', printing_large, name='printing_large'),
    path('promotional_products/', promotional_products, name='promotional_products'),
    path('markirovka/', markirovka, name='markirovka'),
    path('poligraphy_product/<int:pk>/', poligraphy_product,  name='poligraphy_product'),
    path('printing_paper/', printing_paper,  name='printing_paper'),
    path('printing_textile/', printing_textile, name='printing_textile'),
    path('textile_products/', textile_products, name='textile_products'),
    path('advertisement/', aboutview, name='advertisement'),
    # path('application_order/', test_form, name='application_order'),
    path('all/', Home.as_view(), name='all'),
    path('create/', createView, name="create"),
    path('list/', listView, name="list"),
    path('user_login_view/', user_login, name='login'),
    path('create-pdf/', ViewPDF.as_view(), name="create_pdf"),
    path('aboutview/', aboutview, name='aboutview'),
    path('servicecategory/', servicecategory, name='servicecategory'),
    path('type-service/<int:pk>/', service_type, name='type_service'),
    path('typeimage/<int:pk>',typeimage,name='typeimage'),
]
