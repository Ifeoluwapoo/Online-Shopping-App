# Create your views here.
from django.http import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.template import RequestContext
from django.template.loader import render_to_string
from django.forms.models import model_to_dict
from django.contrib.auth import authenticate, login, logout
from cart.forms import CartAddProductForm


from datetime import datetime
from .models import Category, Product, MainCategory, SubCategory
from .forms import ContactForm, LoginForm, RegisterForm, AddProductForm, EditProductForm, ViewProductForm


def indexPage(request, category_slug=None):
    category = None
   # mainCategory = None
    #subCategory = None
    categories = Category.objects.all()
    maincategories = MainCategory.objects.all()
    subcategories = SubCategory.objects.all()
    cart_product_form = CartAddProductForm()
    products = Product.objects.filter(available=True, is_deleted = False)
    # if category_slug:
    #     category = get_object_or_404(Category, slug=category_slug)
    #     products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'maincategories': maincategories,
        'subcategories': subcategories,
        'cart_product_form': cart_product_form,
        'products': products
    }
    return render(request, "onlineShopTemplate/index.html", context)

def aboutPage(request):
    return render(request, "onlineShopTemplate/about.html")


#Loading product on the subcategory Desktop to the page
def desktopPage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'Desktops')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/desktops.html", context)


#Loading product on the subcategory laptop to the page
def laptopPage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'Laptops')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/laptops.html", context)


#Loading product on the subcategory computer Accessories to the page
def compAccessPage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'Computer Access')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/computerAccess.html", context)


#Loading product on the subcategory android to the page
def androidPage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'Android Phones')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/androidPhones.html", context)


#Loading product on the subcategory iosPhones to the page
def iosPhonePage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'iPhones')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/iosPhones.html", context)


#Loading product on the subcategory Phone Accessories to the page
def phoneAccessPage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'Phone Access')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/phoneAccess.html", context)


#Loading product on the subcategory Android Tablet to the page
def androidTabletPage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'Android Tablet')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/androidTablets.html", context)


#Loading product on the subcategory ios Tablets to the page
def iosTabletPage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'iOS Tablet')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/iosTablets.html", context)


#Loading product on the subcategory Tablet Accessories to the page
def tabletAccessPage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'Tablet Access')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/tabletAccess.html", context)


#Loading product on the subcategory TV and Play Stations to the page
def tv_playstationPage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'TV & Play Stations')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/tv_playstations.html", context)


#Loading product on the subcategory AC, Fridges, Freezers to the page
def ac_fridgesPage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'AC and Fridge')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/ac_fridges.html", context)


#Loading product on the subcategory washing machines to the page
def washingMachinePage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'Washing Machine')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/washing_machines.html", context)


#Loading product on the subcategory TV and Play Stations to the page
def cookerPage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'Cookers')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/cookers.html", context)


#Loading product on the subcategory Grinders and blenders to the page
def grinderPage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'Grinder')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/grinders.html", context)


#Loading product on the subcategory kitchen utensils to the page
def utensilPage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'Utensils')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/utensils.html", context)


#Loading product on the subcategory Power (Generators,) to the page
def powerPage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'Power')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/powers.html", context)


#Loading product on the subcategory house seater, dinning set to the page
def house_seaterPage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'House Seaters')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/house_seater.html", context)


#Loading product on the subcategory washing machines to the page
def electricAccessPage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'Washing Machine')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/electrical_access.html", context)


#Loading product on the subcategory Men Bags to the page
def menBagPage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'Men Bags')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/menBags.html", context)


#Loading product on the subcategory Men Dresses to the page
def menDressPage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'Men Dresses')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/menDresses.html", context)


#Loading product on the subcategory Men Shoes to the page
def menShoePage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'Men Shoes')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/menShoes.html", context)

#Loading product on the subcategory Women Bags to the page
def womenBagPage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'Women Bags')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/womenBags.html", context)


#Loading product on the subcategory Women Dresses to the page
def womenDressPage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'Women Dresses')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/womenDresses.html", context)


#Loading product on the subcategory Women Shoes to the page
def womenShoePage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'Women Shoes')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/womenShoes.html", context)


#Loading product on the subcategory Beddings to the page
def beddingsPage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'Beddings')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/beddings.html", context)


#Loading product on the subcategory Women Accessories to the page
def womenAccessoriesPage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'Women Access')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/women_access.html", context)


#Loading product on the subcategory Men Accessories to the page
def menAccessoriesPage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'Men Access')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/men_access.html", context)


#Loading product on the subcategory New Born Dresses to the page
def newbornDressPage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'NewBorn Dresses')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/newborn_dress.html", context)


#Loading product on the subcategory New Born shoes to the page
def newbornShoePage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'NewBorn Shoes')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/newborn_shoes.html", context)


#Loading product on the subcategory New Born Diapers to the page
def newbornDiaperPage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'NewBorn Diapers')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/newborn_diapers.html", context)


#Loading product on the subcategory Kid Dresses to the page
def kidsDressPage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'Kid Dresses')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/kid_dress.html", context)


#Loading product on the subcategoryKid shoes to the page
def kidsShoePage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'Kid Shoes')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/kid_shoes.html", context)


#Loading product on the subcategory Toys to the page
def toyPage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'Kid Toy')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/toys.html", context)


#Loading product on the subcategory New Born Accessories to the page
def newbornAccessPage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'NewBorn Access')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/newborn_Access.html", context)


#Loading product on the subcategory Kid Accessories to the page
def kidAccessPage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'Kid Access')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/kid_access.html", context)


#Loading product on the subcategory Baby Carriage to the page
def babyCarriagePage(request):
    product = Product.objects.filter(available=True, is_deleted = False, sub_category__name = 'Baby Carriage')
    context = {
        'subcategories': product,
    }
    return render(request, "onlineShopTemplate/items/carriage.html", context)


def product1Page(request):
    return render(request, "onlineShopTemplate/products.html")

# Individual ProductDetail added to cart
def productDetailPage(request, pk):
    product = get_object_or_404(Product, pk=pk, is_deleted=False, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    print(context)
    return render(request, "onlineShopTemplate/productDetails.html", context)


#Displays the contact us Page
def contactPage(request):
    return render(request, "onlineShopTemplate/contact.html")

class AddProductView(CreateView):
    model = Product
    form_class = AddProductForm
    template_name = "onlineShopTemplate/myadmin/addProduct.html"
    print(form_class)
    success_url = reverse_lazy('product_list')


#Loads subcategories and categories on the add product by the Admin (An ajax call)
def load_categories(request):
    main_category = request.GET.get('main_category')
    category = Category.objects.filter(main_category_id=main_category).order_by('name')
    category_name = request.GET.get('category')
    if category_name != None:
        sub_category = SubCategory.objects.filter(category_id =category_name).order_by('name')
        return render(request, 'onlineShopTemplate/myadmin/subcategories.html', {"subcategories": sub_category})
    
    return render(request, 'onlineShopTemplate/myadmin/categories.html', {'categories': category})


class AdminProductListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    permission_denied_message = "You are not allowed here."
    model = Product
    template_name = "onlineShopTemplate/myadmin/listProducts.html"
    context_object_name = 'products'  # Default: object_list
    paginate_by = 10
    queryset = Product.objects.filter(is_deleted=False).order_by('-created_at')
#   Product.objects.all();
    # def get_login_url(self):
    #     staff = self.request.user.is_staff
    #     if staff.is_authenticated():
    #     #if not self.request.user.is_staff:
    #         # User is logged in but does not have permission
    #         return redirect ('onlineShopTemplate/registration/login.html')
    #     else:
    #         # User is not logged in 
    #          return "You are not allowed here."       
           

     
def ViewProduct(request, pk):
    
    # Either render only the modal content, or a full standalone page
    if request.is_ajax():
        template_name = 'onlineShopTemplate/myadmin/viewProduct.html'
    else:
        template_name = None

    product = get_object_or_404(Product, pk=pk)

    form = ViewProductForm(request.FILES or None, instance=product)
    form.fields['main_category'].disabled = True
    form.fields['category'].disabled = True
    form.fields['sub_category'].disabled = True
    form.fields['name'].disabled = True
    form.fields['brand'].disabled = True
    form.fields['quantity'].disabled = True
    form.fields['description'].disabled = True
    form.fields['manufacturer'].disabled = True
    form.fields['price'].disabled = True
    form.fields['image'].disabled = True
    return render(request, template_name, {
        'product': product,
        'form': form,
    })  
# instance=request.user.userprofilemodel

def UpdateProduct(request, pk):
    # Either render only the modal content, or a full standalone page
    if request.is_ajax():
        template_name = 'onlineShopTemplate/myadmin/editProduct.html'
    else:
        template_name = None

    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = EditProductForm(request.POST or None, request.FILES or None,  instance=product)
        if form.is_valid():
            form.save()

    else:
        form = EditProductForm(instance=product)
        print(form)

    return render(request, template_name, {
        'product': product,
        'form': form,
    })

def DeleteProduct(request, pk):
    if request.is_ajax():
        template_name = 'onlineShopTemplate/myadmin/deleteProduct.html'

    product = get_object_or_404(Product, pk=pk)
    form = EditProductForm(instance=product)
    if request.method == 'POST':
        product.is_deleted = True
        product.deleted_at = datetime.now()
        product.save()
        return redirect('product_list')

    return render(request, template_name, {
        'product': product,
        'form': form,
    })

# def login_user(request):
#     logout(request)
#     username = password = ''
#     if request.POST:
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(username=username, password=password)
#         print(user)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect('onlineShopTemplate/myadmin/listProducts.html')
#     #return render_to_response('onlineShopTemplate/registration/login.html', context_instance=RequestContext(request))
#     return render_to_response('onlineShopTemplate/registration/login.html')
    

# def login_user(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         if user.is_active:
#             login(request, user)
#             return redirect('onlineShopTemplate/myadmin/listProducts.html')
#             # Redirect to a success page.
#         else:
#             # Return a 'disabled account' error message
#             return redirect('onlineShopTemplate/myadmin/login.html')
            
#     else:
#         # Return an 'invalid login' error message.
#         return redirect('onlineShopTemplate/myadmin/login.html')


# class UpdateProductView(UpdateView):ViewProductForm
#     model = Product
#     form_class = EditProductForm
#     template_name = 'onlineShopTemplate/myadmin/editProduct.html'
#     print(Product.id)

#     def dispatch(self, *args, **kwargs):
#         self.id = kwargs['pk']
#         return super(EditProductView, self).dispatch(*args, **kwargs)

#     def form_valid(self, form):
#         form.save()
#         product = Product.objects.get(id=self.id)
#         return HttpResponse(redirect('product_list', {'product': product}))

# class PersonUpdateView(UpdateView):
#     model = Product
#     fields = ('name', 'birthdate', 'country', 'city')
#     success_url = reverse_lazy('person_changelist')


# def paging(request):
#     prodduct_list = Product.objects.all()
#     page = request.GET.get('page', 1)

#     paginator = Paginator(prodduct_list, 10)
#     try:
#         products = paginator.page(page)
#     except PageNotAnInteger:
#         products = paginator.page(1)
#     except EmptyPage:
#         products = paginator.page(paginator.num_pages)

#     return render(request, 'core/user_list.html', { 'users': products })


# def AddProductView(request):  
#     if request.method == "POST":  
#         form = AddProductForm(request.POST, request.FILES or None)

#         cat_name_list = request.POST.getlist('category', None)
#         selected_cat_obj_list = Category.objects.filter(pk__in= cat_name_list)
#         Product.category = Category.objects.get(name = selected_cat_obj_list[0])
        
#         #Product.category = Category.objects.get(name = category)

#         subCat_name_list = request.POST.getlist('sub_category', None)
#         selected_subCat_obj_list = SubCategory.objects.filter(pk__in= subCat_name_list)
#         Product.sub_category = SubCategory.objects.get(name = selected_subCat_obj_list[0])
        
#         #Product.sub_category = SubCategory.objects.get(name = sub_category)

#         # form.category = Product.category
#         # form.sub_category = Product.sub_category
#         print(form)  
#         if form.is_valid():  
#             try: 
#                 post = form.save(commit = False)
#                 post.available = True
#                 post.created_at = datetime.now()
#                 post.updated_at = datetime.now()
#                 post.save()  
#                 return redirect('/onlineShopTemplate/myadmin/listProducts.html')  
#             except:  
#                 pass  
#     else:  
#         form = AddProductForm()  
#     return render(request,'onlineShopTemplate/myadmin/addProduct.html',{'form':form})





# def AddProductView(request):
#     form = form = AddProductForm(request.POST, request.FILES or None)
#     context = {
#      "form": form,
#     }
#     if request.method == "POST":
        
       
#         # mainCat_name_list = request.POST.getlist('main_category', None)
#         # selected_mainCat_obj_list = MainCategory.objects.filter(name__in= mainCat_name_list)
#         main_category = request.POST.get('main_category')
#         Product.main_category = MainCategory.objects.get(name = main_category)
#         print(main_category)

#         # cat_name_list = request.POST.getlist('category', None)
#         # selected_cat_obj_list = Category.objects.filter(name__in= cat_name_list)
#         category = request.POST.get('category')
#         Product.category = Category.objects.get(name = category)
#         #print(category)
#         #print(catName)

#         # subCat_name_list = request.POST.getlist('sub_category', None)
#         # selected_subCat_obj_list = SubCategory.objects.filter(name__in= subCat_name_list)
#         sub_category = request.POST.get('sub_category')
#         Product.sub_category = SubCategory.objects.get(name =  sub_category)
#         print(sub_category)

#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         quantity = request.POST.get('quantity')
#         price = request.POST.get('price')
#         brand = request.POST.get('brand')
#         manufacturer = request.POST.get('manufacturer')
#         image = request.POST.get('image')
#         Product.objects.create(
#                                category = category,
#                                main_category = main_category,
#                                sub_category = sub_category,
#                                quantity = quantity,
#                                price = price,
#                                name = name,
#                                description = description,
#                                brand = brand,
#                                manufacturer = manufacturer,
#                                image = image,
#                                )
#         if form.is_valid():
#             post = form.save(commit = False)
#             # post.category = Product.category,
#             # post.main_category = Product.main_category,
#             # post.sub_category = Product.sub_category,
#             # post.quantity = quantity,
#             # post.price = price,
#             # post.name = name,
#             # post.description = description,
#             # post.brand = brand,
#             # post.manufacturer = manufacturer,
#             # post.image = image,
#             post.available = True
#             post.created_at = datetime.now()
#             post.updated_at = datetime.now()
#             # Finally write the changes into database 
#             #print(form.cleaned_data)
#             post.save()  
#             return render(request, "onlineShopTemplate/myadmin/listProducts.html",  context) 
                   
#         # else: 
#         #      print(form)
#         #     # Redirect back to the same page if the data was invalid 
#         #      return HttpResponse("Sorry an error occurred")

#     return render(request, "onlineShopTemplate/myadmin/addProduct.html",  context)

# check well


#  product_name = form.cleaned_data.get("product_name")
#         main_category = form.cleaned_data.get("main_category")
#         category = form.cleaned_data.get("category")
#         sub_category = form.cleaned_data.get("sub_category")
#         brand = form.cleaned_data.get("brand")
#         quantity = form.cleaned_data.get("quantity")
#         description = form.cleaned_data.get("description")
#         manufacturer = form.cleaned_data.get("manufacturer")
#         price = form.cleaned_data.get("price")
#         image = form.cleaned_data.get("image")
 #formatedDate = myDate.strftime("%Y-%m-%d %H:%M:%S")

# def get_mainCat_name(self):
#         ''' returns the name of the selected language '''
#         try:
#                 return Product.objects.get(id=self.initial['main_category']).name
#         except:
#                 return None

# def AdminProductListView(request):
#     queryset = Product.objects.all()
#     context = {
#         'items_list': queryset
#     }
#     return render(request, "onlineShopTemplate/myadmin/listProducts.html", context)