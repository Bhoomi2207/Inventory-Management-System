from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='dashboard-index'),
    path('products/', views.products, name='dashboard-products'),
    path('products/delete/<int:pk>/', views.product_delete,
         name='dashboard-products-delete'),
    path('products/detail/<int:pk>/', views.product_detail,
         name='dashboard-products-detail'),
    path('products/edit/<int:pk>/', views.product_edit,
         name='dashboard-products-edit'),
    path('customers/', views.customers, name='dashboard-customers'),
    path('customers/detail/<int:pk>/', views.customer_detail,
         name='dashboard-customer-detail'),
    path('customers/edit/<int:pk>/', views.customer_edit,
         name='dashboard-customer-edit'),
    path('customers/delete/<int:pk>/', views.customer_delete,
         name='dashboard-customer-delete'),
    path('order/', views.order, name='dashboard-order'),
]
