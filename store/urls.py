from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),

    # 🔐 Seller panel (mobile)
    path('seller/', views.seller_login, name='seller_login'),
    path('seller/dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('seller/logout/', views.seller_logout, name='seller_logout'),
    path('seller/product/<int:pk>/edit/', views.seller_edit_product, name='seller_edit_product'),
]
