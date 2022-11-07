from distutils.command.upload import upload
from django.utils.translation import gettext_lazy as _
from unicodedata import category
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.core.validators import FileExtensionValidator



class MyUserManager(BaseUserManager):


    def create_user(self, first_name, phone_number, password=None):
        if not phone_number:
            raise ValueError('Users must have an phone number')
        user = self.model(
            first_name=first_name,
            phone_number = phone_number

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name,phone_number,  password):
        user = self.create_user(first_name,phone_number, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_('first_name'), max_length=64, blank=True)
    full_name = models.CharField(_('full_name'), max_length=64, blank=True)
    phone_number = models.IntegerField(_('phone_number'), blank=True, unique=True)
    email = models.EmailField(verbose_name='email address', null=True, max_length=25)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name']

    objects = MyUserManager()

    def get_full_name(self):
        return self.full_name

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Manager')
        verbose_name_plural = _('Managers')

    def __str__(self) -> str:
        return str(self.phone_number)

    def save(self, *args, **kwargs):
        # password = self.password
        # self.set_password(password)
        return super(User,self).save(*args, **kwargs)



#detail product
class InfoProduct(models.Model):
    size = models.CharField(_('size'), max_length=65)
    element = models.CharField(_('element'), max_length=65)


    def __str__(self):
        return self.size


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Sub Category")


#Product
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(_('name'), max_length=65)
    image = models.ImageField(_('image'), upload_to='media/product')
    info_product = models.ForeignKey(InfoProduct, on_delete=models.CASCADE, blank=True, null=True)
    vendor_code = models.CharField(max_length=20)
    description = models.TextField(_('description'))

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = _("Maxsulot")
        verbose_name_plural = _("Maxsulotlar")

class Product_Orders(models.Model):
    name = models.CharField(max_length=50)
    vendor_code = models.CharField(max_length=50)
    phone = models.CharField(max_length=14)
    creat_add = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Maxsulot zakazi")
        verbose_name_plural = _("Maxsulot zakazlari")




class Type(models.Model):
    name = models.CharField(_('name'), max_length=65)
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Xizmat ko'rsatish turlari")

class Image(models.Model):
    type_sevice = models.ForeignKey(Type, on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(upload_to='media/service', blank=True, null=True)

    def __str__(self):
        return str(self.type_sevice)

    class Meta:
        verbose_name = _("Rasm")
        verbose_name_plural = _("Rasmlar")

# Reklama , Poligrafia, Suviner
class TypeService(models.Model):
    name = models.CharField(_('name'), max_length=65)
    image = models.ImageField(upload_to="media/typeserveis")

    def str(self) -> str:
        return self.name
    class Meta:
        verbose_name = _("Xizmat turi")


class MenuService(models.Model):
    name = models.CharField(_('name'), max_length=65)
    image = models.ImageField(_('image'), upload_to='media/menuservice')
    type_service = models.ForeignKey(TypeService, on_delete=models.CASCADE, blank=True, null=True)

    def str(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Menyu Xizmati")




class Sponsors(models.Model):
    image = models.FileField(upload_to="media/pictures/%Y/%m/", validators=[FileExtensionValidator(['pdf', 'doc', 'svg'])])


    class Meta:
        verbose_name = _("Sponsors")



#Наши работы.
class Portfolio(models.Model):
    name = models.CharField(_('name'), max_length=65)
    image = models.ImageField(_('image'), upload_to='media/portfolio')

    def __str__(self) -> str:
                return self.name
    class Meta:
        verbose_name = _("Portfolio")


class Customer(models.Model):
    id_name_order = models.CharField(_('id_name_order'), max_length=300)
    client = models.CharField(_('client'), max_length=65)
    client_phone_number = models.CharField(_('client_phone_number'), max_length=65)
    manager_name = models.CharField(_('manager_name'), max_length=65)
    date_order = models.DateTimeField(_('date_order'), auto_now_add=False)
    ready_product_date_order = models.DateTimeField(_('ready_product_date_order'), auto_now_add=False)


    def __str__(self):
        return self.client

    class Meta:
        db_table = _('customers')  


class OrderForm(models.Model):
    student = models.ForeignKey(Customer, related_name = "orders", on_delete=models.CASCADE)
    Product_Status = (
        ('ta', 'ta'),
        ('kg', 'kg'),
    )
    name = models.CharField(_('name'), max_length=65, blank=True, null=True)
    status_order = models.CharField(_('status_order'), max_length=20, choices=Product_Status, default='шт', null=True, blank=True)
    amount = models.IntegerField(_('amount'), blank=True, null=True)
    price = models.PositiveIntegerField(_('price'), blank=True, null=True)
    price_free_VAT = models.PositiveIntegerField(_('price_free_VAT'), blank=True, null=True)
    VAT = models.FloatField(_('VAT'), blank=True, null=True)
    price_with_VAT = models.PositiveIntegerField(_('price_with_VAT'), blank=True, null=True)
    total = models.PositiveIntegerField(_('total'), blank=True, null=True)
    total_price_with_VAT = models.PositiveIntegerField(_('total_price_with_VAT'), blank=True, null=True)
    total_price_ALL = models.PositiveIntegerField(_('total_price_ALL'), blank=True, null=True)

    @property
    def total_sum(self):
        summ = self.price * self.amount
        return summ
    @property
    def total_sum_wit_nds(self):
        total_summ_with_nds = (self.total_sum)/100 * self.VAT + self.total_sum
        return total_summ_with_nds

    @property
    def without_percent_price(self):
        sume = self.price * self.amount
        return sume

    def __str__(self) -> str:
                return self.name

    class Meta:
        db_table = _('orders')






class Settings(models.Model):
    key = models.CharField(_('key'), max_length=50, primary_key=True)
    value = models.TextField(_('value'))
    class Meta:
        verbose_name = _("Sozlama")
        verbose_name_plural = _("Sozlamalar")



class About(models.Model):
    description = models.TextField(_('description_uz'), blank=True, null=True)
    def str(self):
        return self.description

    class Meta:
        verbose_name = _("Biz Haqimizda")

class AboutImage(models.Model):
    name = models.CharField(_('name_uz'), max_length=60, blank=True, null=True)
    image = models.ImageField(_('image'), upload_to='media/about', blank=True, null=True)
    def str(self):
        return self.name



class OrderService(models.Model):
    order_type = models.ForeignKey(Type, on_delete=models.CASCADE, blank=True, null=True)
    username = models.CharField(_('full_name'), max_length=65)
    phone_number = models.CharField(_('phone_number'), max_length=15)
    files = models.FileField(_('files'), upload_to='media/file', max_length=100, blank=True, null=True)
    creat_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    class Meta:
        verbose_name = _("Xizmat ko'rsatish zakazlari")

#####################################################################################################################################

class Design(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField(max_length=50, blank=True, null=True)
    description = models.TextField()
    image1 = models.ImageField(upload_to="media/serviceee", blank=True, null=True)
    image2 = models.ImageField(upload_to="media/serviceee", blank=True, null=True)
    image3 = models.ImageField(upload_to="media/serviceee", blank=True, null=True)

    def str(self):
        return self.name

    class Meta:
        verbose_name = _("Dizayn")


class DigitalPrint(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="media/serviceee", blank=True, null=True)

    def str(self):
        return self.name

    class Meta:
        verbose_name = _("Raqamli chop etish")


class SubDigitalPrint(models.Model):
    size = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    on_site_print = models.CharField(max_length=50)
    double_site_print = models.CharField(max_length=50)
    all1 = models.ForeignKey(DigitalPrint, on_delete=models.CASCADE)

    def str(self):
            return self.product_name


class LargeFormat(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="media/serviceee", blank=True, null=True)
    image1 = models.ImageField(upload_to="media/serviceee", blank=True, null=True)
    image2 = models.ImageField(upload_to="media/serviceee", blank=True, null=True)
    image3 = models.ImageField(upload_to="media/serviceee", blank=True, null=True)
    
    
    def str(self):
        return self.name



class SubLargeFormat(models.Model):
    product_name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    
    all = models.ForeignKey(LargeFormat, on_delete=models.CASCADE)

    def str(self):
            return self.product_name





class TextPrint(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField(max_length=50, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(max_length=50, upload_to="media/serviceee", blank=True, null=True)
    
    def str(self):
        return self.name
    
    class Meta:
        verbose_name = _("Tekstilni chop etish")


class SUbTextPrint(models.Model):
    size = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    txt = models.ForeignKey(TextPrint, on_delete=models.CASCADE)

    def str(self):
        return self.size

class LaserPrint(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField(max_length=50, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(max_length=50, upload_to="media/serviceee", blank=True, null=True)
    
    def str(self):
        return self.name
    
    class Meta:
        verbose_name = _("Lazerni chop etish")


class SubLaserPrint(models.Model):
    size = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    chain = models.ForeignKey(LaserPrint, on_delete=models.CASCADE)




class Image2(models.Model):
    type_sevice = models.ForeignKey(Type, on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(upload_to='media/service', blank=True, null=True)

    def str(self):
        return str(self.type_sevice)

    class Meta:
        verbose_name = _("Xizmat ko'rsatish rasmlari")


