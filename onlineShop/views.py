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


def product1Page(request):
    return render(request, "onlineShopTemplate/products.html")

# Individual ProductDetail


def productDetailPage(request, pk):
    product = get_object_or_404(Product, pk=pk, is_deleted=False, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    print(context)
    return render(request, "onlineShopTemplate/productDetails.html", context)

# class productDetailPage(DetailView):
#     model = Product
#     template_name = "onlineShopTemplate/productDetails.html"
#     context_object_name = "product"

def contactPage(request):
    return render(request, "onlineShopTemplate/contact.html")

class AddProductView(CreateView):
    model = Product
    form_class = AddProductForm
    template_name = "onlineShopTemplate/myadmin/addProduct.html"
    print(form_class)
    success_url = reverse_lazy('product_list')


def load_categories(request):
    main_category = request.GET.get('main_category')
    category = Category.objects.filter(main_category_id=main_category).order_by('name')
    #category = Category.objects.filter(main_category__name =main_category).order_by('name')
    category_name = request.GET.get('category')
    if category_name != None:
        sub_category = SubCategory.objects.filter(category_id =category_name).order_by('name')
        #sub_category = SubCategory.objects.filter(category__name =category_name).order_by('name')
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