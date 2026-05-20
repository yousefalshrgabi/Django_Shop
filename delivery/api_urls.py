# from django.urls import path
# from .views import DeliveryAPIListCreateView, DeliveryAPIDetailView

# # ============================================================
# # 🌐 API URL Patterns — Delivery
# # ============================================================
# # الـ namespace: delivery_api
# # Base URL: /api/delivery/
# #
# # المسارات المتاحة:
# #   GET    /api/delivery/       → قائمة جميع السائقين (JSON)
# #   POST   /api/delivery/       → إنشاء سائق جديد
# #   GET    /api/delivery/<pk>/  → بيانات سائق محدد
# #   PUT    /api/delivery/<pk>/  → تعديل كامل لسائق
# #   PATCH  /api/delivery/<pk>/  → تعديل جزئي لسائق
# #   DELETE /api/delivery/<pk>/  → حذف سائق
# # ============================================================

# urlpatterns = [
#     path('', DeliveryAPIListCreateView.as_view(), name='api_delivery_list'),
#     path('<int:pk>/', DeliveryAPIDetailView.as_view(), name='api_delivery_detail'),
# ]
