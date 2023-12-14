from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_summary, name='cart_summary'),
    path('add/<uuid:book_id>/', views.cart_add, name='cart_add'),
    path('cart/delete/<int:purchase_id>/', views.cart_delete, name='cart_delete'),
    path('cart_summary/', views.cart_summary, name='cart_summary'),
    path('update/', views.cart_update, name='cart_update'),
    path('checkout/', views.checkout, name='checkout'),
    path('success/', views.success, name='success'),
    path('order_history/', views.order_history, name='order_history'),
] 