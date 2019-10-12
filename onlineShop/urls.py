#from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, logout_then_login, LogoutView
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from onlineShop import views
#from products.views import ProductListView, product_list_view, ProductDetailView, product_detail_view

#Url routes are case sensitive
urlpatterns = [

    path("", views.indexPage, name="index"),
    path("about/", views.aboutPage, name="about"),
    path("products/", views.product1Page, name="products"),

    #Each product page URL

    path("items/androidPhones/", views.androidPage, name="androidphones"),
    path("items/desktops/", views.desktopPage, name="desktops"),
    path("items/laptops/", views.laptopPage, name="laptops"),
    path("items/computerAccess/", views.compAccessPage, name="computerAccess"),
    path("items/iosPhones/", views.iosPhonePage, name="iosphones"),
    path("items/phoneAccess/", views.phoneAccessPage, name="phoneAccess"),
    path("items/androidTablets/", views.androidTabletPage, name="androidTablets"),
    path("items/iosTablets/", views.iosTabletPage, name="iosTablets"),
    path("items/tabletAccess/", views.tabletAccessPage, name="tabletAccess"),
    path("items/tv_playstations/", views.tv_playstationPage, name="tvPlaystations"),
    path("items/ac_fridges/", views.ac_fridgesPage, name="acFridges"),
    path("items/washing_machines/", views.washingMachinePage, name="washingMachines"),
    path("items/grinders/", views.grinderPage, name="grinders"),
    path("items/cookers/", views.cookerPage, name="cookers"),
    path("items/utensils/", views.utensilPage, name="utensils"),
    path("items/powers/", views.powerPage, name="powers"),
    path("items/house_seater/", views.house_seaterPage, name="houseSeater"),
    path("items/electric_access/", views.electricAccessPage, name="electricAccess"),
    path("items/menDresses/", views.menDressPage, name="mendress"),
    path("items/menBags/", views.menBagPage, name="menbags"),
    path("items/menShoes/", views.menShoePage, name="menshoes"),
    path("items/womenDresses/", views.womenDressPage, name="womendress"),
    path("items/womenBags/", views.womenBagPage, name="womenbags"),
    path("items/womenShoes/", views.womenShoePage, name="womenshoes"),
    path("items/beddings/", views.beddingsPage, name="beddings"),
    path("items/women_access/", views.womenAccessoriesPage, name="womenaccess"),
    path("items/men_access/", views.menAccessoriesPage, name="menaccess"),
    path("items/newborn_dress/", views.newbornDressPage, name="newbornDress"),
    path("items/newborn_shoes/", views.newbornShoePage, name="newbornShoes"),
    path("items/newborn_diapers/", views.newbornDiaperPage, name="newbornDiaper"),
    path("items/kid_dress/", views.kidsDressPage, name="kidDress"),
    path("items/kid_shoes/", views.kidsShoePage, name="kidShoes"),
    path("items/toys/", views.toyPage, name="toys"),
    path("items/newborn_Access/", views.newbornAccessPage, name="newbornAccess"),
    path("items/kid_access/", views.kidAccessPage, name="kidAccess"),
    path("items/carriage/", views.babyCarriagePage, name="babyCarriage"),
    
    


    #path("productDetails/", views.productDetailPage, name="productDetails"),
    url(r'^productDetails/(?P<pk>\d+)/$', views.productDetailPage, name='productDetails'),


    path("contact/", views.contactPage, name="contact"),
    url(r'^myadmin/$', views.AdminProductListView.as_view(), name='product_list'),
    url(r'^myadmin/addProduct/$', views.AddProductView.as_view(), name='product_add'),
    url(r'^myadmin/viewProduct/(?P<pk>\d+)/$', views.ViewProduct, name='product_view'),
    url(r'^myadmin/editProduct/(?P<pk>\d+)/$', views.UpdateProduct, name='product_edit'),
    url(r'^myadmin/deleteProduct/(?P<pk>\d+)/$', views.DeleteProduct, name='product_delete'),

    #Log in Urls
    #url(r'^registration/login/$', views.login_user, name='login'),
    #url(r'^login/$', auth_views.login, name='login'),
    #url(r'^login/$', auth_views.LoginView, {'template_name': 'registration/login.html'}, name='login'),
    #url(r'^logout/$', auth_views.logout, name='logout'),
    #url(r'^admin/', include('django.contrib.admin.urls')),
    url(r'^login/$', LoginView.as_view(), {'template_name': 'onlineShopTemplate/registration/login.html'}, name='login'),
    url(r'^admin/', admin.site.urls),
    

    path('ajax/load_categories/', views.load_categories, name='ajax_load_categories'),
    #path('ajax/load_subcategories/', views.load_subcategories, name='ajax_load_subcategories'),
    #path("contact/", views.contact, name="contact"),
]
