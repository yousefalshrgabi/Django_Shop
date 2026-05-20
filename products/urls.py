from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    # عرض قائمة المنتجات - يتطلب تسجيل الدخول فقط
    path('', views.ProductListView.as_view(), name='product_list'),
    # إضافة منتج جديد - يتطلب صلاحية add_product
    path('add/', views.ProductCreateView.as_view(), name='product_create'),
    # تعديل منتج - يتطلب صلاحية change_product
    path('edit/<int:pk>/', views.ProductUpdateView.as_view(), name='product_update'),
    # حذف منتج - يتطلب صلاحية delete_product
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),
]
