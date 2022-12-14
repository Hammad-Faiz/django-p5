from venv import create
from . import views
from django.urls import path



urlpatterns = [
    path('',views.index, name="index"),
    path('<int:id>', views.show, name="show"),
    path('create',views.create, name="create"),
    path('update-product/<int:id>',views.updateProduct, name='update-product'),
    path('delete-product/<int:id>',views.deleteProduct, name='delete-product'),
    path('profile',views.profile, name="profile"),
    path('cart',views.cart, name='cart'),
    path('checkout',views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name='process_order'),
    path('orders/',views.orders, name='orders')
]
