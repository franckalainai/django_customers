from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products),
    path('customer/<str:pk_test>/', views.customer),
    path('create_order/', views.createOrder, name='create-order'),
    path('update_order/<str:pk>', views.updateOrder, name='update-order'),
    path('delete_order/<str:pk>', views.deleteOrder, name='delete-order'),

]