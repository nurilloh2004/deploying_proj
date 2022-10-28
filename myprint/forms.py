from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import ModelForm

from .models import *

# class OrForm(forms.ModelForm):
#     class Meta:
#         model = Form
#         fields = [
# 			'full_name',
# 			'phone_number',
# 		]


class OrderServiceForm(forms.ModelForm):
    class Meta:
        model = OrderService
        exclude = ['creat_add']

        widgets = {
            'files': forms.FileInput(attrs={
                "accept": ".xlsx,.xls,image/*,.doc,audio/*,.docx,video/*,.ppt,.pptx,.txt,.pdf",
                "type": "file"
            }),

            'order_type': forms.Select(attrs={
                'class': 'custom-select',

            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control mt-4',
                'placeholder': 'Имя...'
            }),
            'phone_number': forms.NumberInput(attrs={
                'class': 'form-control mt-3',
                'maxlength': '13',
                'placeholder': 'Телефон...',
                'value': '+998'
            })
        }
# class OrForm(forms.Form):
#     class Meta:
#         model = Form

#     widgets = {
#             'full_name': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'ФИШ'
#             }),
#             'phone_number': forms.NumberInput(attrs={
#                 'class': 'form-control mt-3 mb-3',
#                 'placeholder': 'Telefon',
#             })
#         }



class CustomerForm(forms.ModelForm):
    id_name_order = forms.CharField(required=True)
    client = forms.CharField(required=True)
    client_phone_number = forms.CharField(required=True)
    manager_name = forms.CharField(required=True)
    date_order = forms.CharField(required=True)
    ready_product_date_order = forms.CharField(required=True)

    class Meta:
        model = Customer
        
        fields = [
			'id_name_order',
			'client',
			'client_phone_number',
            'manager_name',
            'date_order',
            'ready_product_date_order',
		]

class OrdersForm(forms.ModelForm):
	class Meta:
		model = OrderForm

		fields = [
			'name',
			'status_order',
            'amount',
            'price',
            'price_free_VAT',
            'VAT',
            'price_with_VAT',
            'total',
		]

		widgets = {
			'name': forms.TextInput(attrs={'class': 'formset-field'}),
			'status_order': forms.TextInput(attrs={'class': 'formset-field'}),
			'price': forms.NumberInput(attrs={'class': 'formset-field'}),
            'price_free_VAT': forms.NumberInput(attrs={'class': 'formset-field'}),
            'VAT': forms.NumberInput(attrs={'class': 'formset-field'}),
            'price_with_VAT': forms.NumberInput(attrs={'class': 'formset-field'}),
            'total': forms.NumberInput(attrs={'class': 'formset-field'}),
		}

class UserLoginForm(forms.Form):
    phone_number = forms.IntegerField(widget=forms.TextInput(attrs={
        "class": 'form-control mb-2 form-control',
        'type': 'number',
        'placeholder': 'Телефон ...'
    }))
    password = forms.CharField(max_length=20,widget=forms.TextInput(attrs={
        "class": 'form-control mb-5',
        'type': 'pasword',
        'placeholder': 'Пароль ...'
    }))
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }

