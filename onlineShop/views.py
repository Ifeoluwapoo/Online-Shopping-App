# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from datetime import datetime
from .models import Category, Product, MainCategory, SubCategory
from .forms import ContactForm, LoginForm, RegisterForm, AddProductForm


def indexPage(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    # if category_slug:
    #     category = get_object_or_404(Category, slug=category_slug)
    #     products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, "onlineShopTemplate/index.html", context)


def aboutPage(request):
    return render(request, "onlineShopTemplate/about.html")


def product1Page(request):
    return render(request, "onlineShopTemplate/products.html")

# Individual ProductDetail


def productDetailPage(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    context = {
        'product': product
    }
    return render(request, "onlineShopTemplate/productDetails.html")


def contactPage(request):
    return render(request, "onlineShopTemplate/contact.html")


# class CreateProductView(CreateView): # new
#     model = Product
#     form_class = AddProductForm
#     template_name = 'onlineShopTemplate/myadmin/addProduct.html'
#     success_url = reverse_lazy('product_list')


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


class AdminProductListView(ListView):
    model = Product
    #queryset = Product.objects.all()
    template_name = "onlineShopTemplate/myadmin/listProducts.html"
    context_object_name = 'products'  # Default: object_list
    paginate_by = 10
    queryset = Product.objects.all() 

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
