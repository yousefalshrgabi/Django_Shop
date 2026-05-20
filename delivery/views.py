from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import Delivery
from .forms import DeliveryForm


# ============================================================
# ⚠ الدوال القديمة (Function-Based Views) - محفوظة كتعليقات
# تم تحويلها إلى Class-Based Views أدناه
# ============================================================

# def delivery_list(request):
#     """عرض قائمة جميع سائقي التوصيل"""
#     delivery = Delivery.objects.all()
#     return render(request, 'delivery/list.html', {'delivery': delivery})

# def delivery_create(request):
#     """إضافة سائق توصيل جديد - GET: عرض النموذج / POST: حفظ البيانات"""
#     if request.method == 'POST':
#         form = DeliveryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('delivery:delivery_list')
#     else:
#         form = DeliveryForm()
#     return render(request, 'delivery/add.html', {'form': form})

# def delivery_update(request, pk):
#     """تعديل بيانات سائق توصيل بواسطة المفتاح الأساسي pk"""
#     delivery = get_object_or_404(Delivery, pk=pk)
#     if request.method == 'POST':
#         form = DeliveryForm(request.POST, instance=delivery)
#         if form.is_valid():
#             form.save()
#             return redirect('delivery:delivery_list')
#     else:
#         form = DeliveryForm(instance=delivery)
#     return render(request, 'delivery/edit.html', {'form': form, 'delivery': delivery})

# def delivery_delete(request, pk):
#     """حذف سائق توصيل بعد التأكيد"""
#     delivery = get_object_or_404(Delivery, pk=pk)
#     if request.method == 'POST':
#         delivery.delete()
#         return redirect('delivery:delivery_list')
#     return render(request, 'delivery/delete.html', {'delivery': delivery})


# ============================================================
# Class-Based Views الجديدة مع نظام الصلاحيات والحماية
# ============================================================

class DeliveryListView(LoginRequiredMixin, View):
    """
    عرض قائمة سائقي التوصيل - متاح لأي مستخدم مسجل دخوله
    LoginRequiredMixin: يحوّل المستخدم غير المسجل لصفحة تسجيل الدخول
    """
    template_name = 'delivery/list.html'

    def get(self, request):
        delivery = Delivery.objects.all()
        return render(request, self.template_name, {'delivery': delivery})


class DeliveryCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """
    إضافة سائق توصيل جديد - يتطلب تسجيل الدخول + صلاحية (delivery.add_delivery)
    PermissionRequiredMixin: يرفض المستخدم الذي لا يملك الصلاحية برمز 403
    """
    template_name = 'delivery/add.html'
    permission_required = 'delivery.add_delivery'
    raise_exception = True

    def get(self, request):
        form = DeliveryForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = DeliveryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('delivery:delivery_list')
        return render(request, self.template_name, {'form': form})


class DeliveryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """
    تعديل بيانات سائق - يتطلب تسجيل الدخول + صلاحية (delivery.change_delivery)
    """
    template_name = 'delivery/edit.html'
    permission_required = 'delivery.change_delivery'
    raise_exception = True

    def get(self, request, pk):
        delivery = get_object_or_404(Delivery, pk=pk)
        form = DeliveryForm(instance=delivery)
        return render(request, self.template_name, {'form': form, 'delivery': delivery})

    def post(self, request, pk):
        delivery = get_object_or_404(Delivery, pk=pk)
        form = DeliveryForm(request.POST, instance=delivery)
        if form.is_valid():
            form.save()
            return redirect('delivery:delivery_list')
        return render(request, self.template_name, {'form': form, 'delivery': delivery})


class DeliveryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """
    حذف سائق - يتطلب تسجيل الدخول + صلاحية (delivery.delete_delivery)
    GET: عرض صفحة تأكيد الحذف / POST: تنفيذ الحذف
    """
    template_name = 'delivery/delete.html'
    permission_required = 'delivery.delete_delivery'
    raise_exception = True

    def get(self, request, pk):
        delivery = get_object_or_404(Delivery, pk=pk)
        return render(request, self.template_name, {'delivery': delivery})

    def post(self, request, pk):
        delivery = get_object_or_404(Delivery, pk=pk)
        delivery.delete()
        return redirect('delivery:delivery_list')


# ============================================================
# 🌐 API Views — Django REST Framework (Generic API Views)
# ============================================================
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import DeliverySerializer


class DeliveryAPIListCreateView(ListCreateAPIView):
    """
    Generic API View لقائمة سائقي التوصيل وإنشاء سائق جديد.

    GET  /api/delivery/
        → يُرجع قائمة جميع السائقين بصيغة JSON تلقائياً

    POST /api/delivery/
        → يتحقق من البيانات ويُنشئ سائقاً جديداً تلقائياً
    """
    # 1. ما هي البيانات التي نريد عرضها؟
    queryset = Delivery.objects.all()

    # 2. كيف نحوّلها إلى JSON؟
    serializer_class = DeliverySerializer


class DeliveryAPIDetailView(RetrieveUpdateDestroyAPIView):
    """
    Generic API View لسائق توصيل محدد (بواسطة pk).

    GET    /api/delivery/<pk>/  → إرجاع بيانات سائق واحد
    PUT    /api/delivery/<pk>/  → تعديل كامل لبيانات السائق
    PATCH  /api/delivery/<pk>/  → تعديل جزئي لبيانات السائق
    DELETE /api/delivery/<pk>/  → حذف السائق
    """
    # 1. ما هي البيانات التي نريد التعامل معها؟
    queryset = Delivery.objects.all()

    # 2. كيف نحوّلها إلى JSON؟
    serializer_class = DeliverySerializer

