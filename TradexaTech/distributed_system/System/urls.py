from django.urls import path

from .import views

urlpatterns = [
    path('',views.home),

    path('users',views.users),

    path('orders',views.orders),

    path('products',views.products),

    path('deleteuser',views.deleteuser),

    path('deleteproducts',views.deleteproducts),
]