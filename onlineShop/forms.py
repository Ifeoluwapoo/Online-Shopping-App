from django import forms
from django.forms import ModelForm, Select, TextInput, NumberInput, Textarea, FileInput, DecimalField
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import Category, Product, SubCategory, MainCategory

User = get_user_model()

class ContactForm(forms.Form):
    fullname = forms.CharField(
            widget=forms.TextInput(
                    attrs={
                        "class": "form-control", 
                        "placeholder": "Your full name"
                    }
                    )
            )
    email    = forms.EmailField(
            widget=forms.EmailInput(
                    attrs={
                        "class": "form-control", 
                        "placeholder": "Your email"
                    }
                    )
            )
    content  = forms.CharField(
            widget=forms.Textarea(
                attrs={
                    'class': 'form-control',
                    "placeholder": "Your message" 
                    }
                )
            )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
                widget=forms.PasswordInput()
            )

class RegisterForm(forms.Form):
    username = forms.CharField()
    email    = forms.EmailField()
    password = forms.CharField(
                widget=forms.PasswordInput()
            )
    password2 = forms.CharField(
                label = "Confirm password",
                widget=forms.PasswordInput()
            )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username = username)
        if qs.exists():
            raise forms.ValidationError("User Name Exists")
            return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email = email)
        if qs.exists():
            raise forms.ValidationError("Email Exists")
            return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password2 != password:
            raise forms.ValidationError("Password must match")
        return data

# def __init__(self,*args,**kwargs):
#         myMainCat = kwargs.pop("main_category")     # client is the parameter passed from views.py
#         super(AddProductForm, self).__init__(*args,**kwargs)
#         self.fields['category'] = forms.ChoiceField(label="Sniffer", choices=[(x.plug_ip, x.MY_DESCRIPTIVE_FIELD) for x in Sniffer.objects.filter(client = myClient)])


class AddProductForm(forms.ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'
    main_category    = forms.ModelChoiceField(
             widget=forms.Select(
                    attrs={
                        "class": "form-control", 
                        "name": "mainCategory",
                        "id":   "id_mainCategory",
                        
                    }
                    ),
                queryset=MainCategory.objects.all().order_by('name'),
                empty_label="Select Main Category",
                #to_field_name="name"

        )
   
    class Meta:
        model = Product
        exclude = ['slug','available', 'created_at', 'updated_at']
        widgets = {

            'category': Select(attrs={
                         "class": "form-control", 
                         "name": "category",
                         "id":   "id_category",
                        
                     }),
                     

            'sub_category': Select(attrs={
                         "class": "form-control", 
                         "name": "subCategory",
                         "id":   "id_subcategory",
                        
                     }),

            'name': TextInput(attrs={
                         "class": "form-control", 
                         "placeholder": "Product Name",
                         "name": "productName",
                         "id": "id_productName",
                        
                     }),

            'brand': TextInput(attrs={
                         "class": "form-control", 
                         "placeholder": "Enter Product Brand",
                         "name": "brand",
                         "id": "id_brand",
                        
                     }),

            'quantity': NumberInput(attrs={
                         "class": "form-control", 
                         "placeholder": "Enter Product Quantity",
                         "name": "quantity",
                         "id": "id_quantity",
                        
                     }),

            'description': Textarea(attrs={
                         'class': 'form-control',
                         "placeholder": "Enter Product Description",
                         "name": "description",
                         "id": "id_description",
                        
                     }),

            'manufacturer': TextInput(attrs={
                          "class": "form-control", 
                          "placeholder": "Enter Product Manufacturer",
                          "name": "manufacturer",
                          "id": "id_manufacturer",
                        
                     }),

            'price': NumberInput(attrs={
                         "class": "form-control", 
                         "placeholder": "Enter Product Price",
                         "name": "price",
                         "id": "id_price",
                        
                     }),

            'image': FileInput(attrs={
                         "name": "image",
                         "id": "id_image", 
                        
                     }),
                
        }
        #fields = ('name', 'birthdate', 'country', 'city')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.none()
        self.fields['sub_category'].queryset = SubCategory.objects.none()

        if 'main_category' in self.data:
            try:
                main_category_id = int(self.data.get('main_category'))
                self.fields['category'].queryset = Category.objects.filter(main_category_id = main_category_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.name:
            self.fields['category'].queryset = self.instance.main_category.category_set.order_by('name')

        if 'category' in self.data:
            try:
                category_id = str(self.data.get('category'))
                self.fields['sub_category'].queryset = SubCategory.objects.filter(category_id = category_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['sub_category'].queryset = self.instance.category.sub_category_set.order_by('name')


def clean_productName(self):
        productName = self.cleaned_data.get("product_name")
        qs = User.objects.filter(product_name = productName)
        if qs.exists():
            raise forms.ValidationError("Product Already Exists")
            return productName


# class AddProductForm(forms.ModelForm):
#     error_css_class = 'error'
#     required_css_class = 'required'
#     class Meta:
#         model = Product
        
#         # field_classes = {
#         #     'main_category': forms.ModelChoiceField,
#         # }
#         # widgets = {
#         #     'main_category': Textarea(attrs={"class": "form-control", 
#         #                                         "name": "mainCategory",
#         #                                         "id":   "id_mainCategory",}),
#         # }


#     main_category    = forms.ModelChoiceField(
#             widget=forms.Select(
#                     attrs={
#                         "class": "form-control", 
#                         "name": "mainCategory",
#                         "id":   "id_mainCategory",
                        
#                     }
#                     ),
#                 # queryset=MainCategory.objects.values_list('name',flat=True).distinct(),
#                 queryset=MainCategory.objects.all().order_by('name'),
#                 empty_label="Select Main Category",
#                 to_field_name="name"

#         )

#     category    = forms.ModelChoiceField(
#             widget=forms.Select(
#                     attrs={
#                         "class": "form-control", 
#                         "name": "category",
#                         "id": "id_category",
#                     }
#                     ),
#                    queryset = Category.objects.none()
#             )

#     sub_category    = forms.ModelChoiceField(
#             widget=forms.Select(
#                     attrs={
#                         "class": "form-control", 
#                         "name": "subCategory",
#                         "id": "id_subcategory",
#                     }
#                     ),
#                     queryset = SubCategory.objects.none(),
#             )

#     name = forms.CharField(
#             widget=forms.TextInput(
#                     attrs={
#                         "class": "form-control", 
#                         "placeholder": "Product Name",
#                         "name": "productName",
#                         "id": "id_productName",
#                     }
#                     )
#             )


#     brand = forms.CharField(
#             widget=forms.TextInput(
#                     attrs={
#                         "class": "form-control", 
#                         "placeholder": "Enter Product Brand",
#                         "name": "brand",
#                         "id": "id_brand",
#                     }
#                     )
#             )

#     quantity    = forms.IntegerField(
#             widget=forms.NumberInput(
#                     attrs={
#                         "class": "form-control", 
#                         "placeholder": "Enter Product Quantity",
#                         "name": "quantity",
#                         "id": "id_quantity",
#                     }
#                     )
#             )

            
#     description  = forms.CharField(
#             widget=forms.Textarea(
#                 attrs={
#                     'class': 'form-control',
#                     "placeholder": "Enter Product Description",
#                     "name": "description",
#                     "id": "id_description",
#                     }
#                 )
#             )

#     manufacturer    = forms.CharField(
#             widget=forms.TextInput(
#                     attrs={
#                         "class": "form-control", 
#                         "placeholder": "Enter Product Manufacturer",
#                         "name": "manufacturer",
#                         "id": "id_manufacturer",
#                     }
#                     )
#             )

#     price    = forms.DecimalField(
#             widget=forms.NumberInput(
#                     attrs={
#                         "class": "form-control", 
#                         "placeholder": "Enter Product Price",
#                         "name": "price",
#                         "id": "id_price",
#                     }
#                     )
#             )
    

#     image   = forms.ImageField(
#             widget = forms.FileInput(
#                     attrs = {
#                         #"class": "form-control",
#                         "name": "image",
#                         "id": "id_image", 
#                     }
#             )

#             )

    # available = forms.BooleanField()

    # def __init__(self):
    #     if check_something():
    #         self.fields['receive_newsletter'].initial  = True

    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['category'].queryset = Category.objects.none()
#         self.fields['sub_category'].queryset = SubCategory.objects.none()
