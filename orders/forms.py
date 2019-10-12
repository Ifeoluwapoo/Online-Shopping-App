from django import forms
from django.forms import ModelForm, TextInput, NumberInput, Textarea, EmailInput
from .models import Order


# class OrderCreateForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'phoneNumber','city']



class OrderCreateForm(forms.ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'
   
    class Meta:
        model = Order
        exclude = ['created','updated', 'paid']
        widgets = {

            'first_name': TextInput(attrs={
                         "class": "form-control", 
                         "placeholder": "Enter your First Name",
                         "name": "firstName",
                         "id": "firstName",
                        
                     }),

            'last_name': TextInput(attrs={
                         "class": "form-control", 
                         "placeholder": "Enter your Last Name",
                         "name": "lastName",
                         "id": "lastName",
                        
                     }),

            'email': EmailInput(attrs={
                         "class": "form-control", 
                         "placeholder": "Enter your Email Address",
                         "name": "email",
                         "id": "email",
                        
                     }),

            'address': Textarea(attrs={
                         'class': 'form-control',
                         "placeholder": "Enter your Address",
                         "name": "address",
                         "id": "address",
                        
                     }),

            'postal_code': TextInput(attrs={
                          "class": "form-control", 
                          "placeholder": "Enter your Postal Code",
                          "name": "postalCode",
                          "id": "postalCode",
                        
                     }),

            'phoneNumber': NumberInput(attrs={
                         "class": "form-control", 
                         "placeholder": "Enter your Phone Number",
                         "name": "phoneNumber",
                         "id": "phoneNumber",
                        
                     }),

             'city': TextInput(attrs={
                          "class": "form-control", 
                          "placeholder": "Enter your City",
                          "name": "city",
                          "id": "city",
                        
                     }),
                
        }