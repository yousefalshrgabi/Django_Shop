"""
URL configuration for shop_stor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import HomeView

urlpatterns = [
    # الصفحة الرئيسية العامة - متاحة للجميع بدون تسجيل دخول
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),

    # ===== صفحات الويب العادية =====
    path('products/', include('products.urls')),
    path('delivery/', include('delivery.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/', include('delivery.urls')),

    # ===== 🌐 API Endpoints =====
    # /api/delivery/       → قائمة + إنشاء سائق
    # /api/delivery/<pk>/  → تفاصيل + تعديل + حذف سائق
    # path('api/delivery/', include('delivery.api_urls')),
]
