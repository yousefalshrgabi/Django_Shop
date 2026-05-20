from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # الصفحة الرئيسية - متاحة للجميع بدون تسجيل دخول
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]

