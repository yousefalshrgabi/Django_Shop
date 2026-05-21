from django.urls import path
from . import views

app_name = 'delivery'

urlpatterns = [
    # عرض قائمة السائقين - يتطلب تسجيل الدخول فقط
    path('', views.DeliveryListView.as_view(), name='delivery_list'),
    # إضافة سائق جديد - يتطلب صلاحية add_delivery
    path('add/', views.DeliveryCreateView.as_view(), name='delivery_create'),
    # تعديل سائق - يتطلب صلاحية change_delivery
    path('edit/<int:pk>/', views.DeliveryUpdateView.as_view(), name='delivery_update'),
    # حذف سائق - يتطلب صلاحية delete_delivery
    path('delete/<int:pk>/', views.DeliveryDeleteView.as_view(), name='delivery_delete'),
    path('delivery/', views.DeliveryAPIListCreateView.as_view(), name='api_delivery_list'),
    path('delivery/<int:pk>/', views.DeliveryAPIDetailView.as_view(), name='api_delivery_detail'),
    # path('create/', views.DeliveryAPIListCreateView.as_view(), name='api_delivery_list_create'),
]
