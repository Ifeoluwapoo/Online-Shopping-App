from django.urls import path
from django.conf.urls import url
from onlineShop import views
#from products.views import ProductListView, product_list_view, ProductDetailView, product_detail_view

#Url routes are case sensitive
urlpatterns = [

    path("", views.indexPage, name="index"),
    path("about/", views.aboutPage, name="about"),
    path("products/", views.product1Page, name="products"),
    path("productDetails/", views.productDetailPage, name="productDetails"),
    path("contact/", views.contactPage, name="contact"),
    url(r'^myadmin/$', views.AdminProductListView.as_view(), name='product_list'),
    url(r'^myadmin/addProduct/$', views.AddProductView.as_view(), name='product_add'),
    url(r'^myadmin/viewProduct/(?P<pk>\d+)/$', views.ViewProduct, name='product_view'),
    url(r'^myadmin/editProduct/(?P<pk>\d+)/$', views.UpdateProduct, name='product_edit'),
    url(r'^myadmin/deleteProduct/(?P<pk>\d+)/$', views.DeleteProduct, name='product_delete'),
    

    path('ajax/load_categories/', views.load_categories, name='ajax_load_categories'),
    #path('ajax/load_subcategories/', views.load_subcategories, name='ajax_load_subcategories'),
    #path("contact/", views.contact, name="contact"),
]
