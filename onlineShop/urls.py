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
