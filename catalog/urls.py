from django.urls import path
from . import views
from django.db.models import Q

app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('search/', views.search_view, name='search'),  # ← вот это нужно!
]
