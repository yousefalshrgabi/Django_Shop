from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm


# ============================================================
# ⚠ الدوال القديمة (Function-Based Views) - محفوظة كتعليقات
# تم تحويلها إلى Class-Based Views أدناه
# ============================================================

# def product_list(request):
#     """عرض قائمة جميع المنتجات"""
#     products = Product.objects.all()
#     return render(request, 'products/list.html', {'products': products})

# def product_create(request):
#     """إنشاء منتج جديد - GET: عرض النموذج / POST: حفظ المنتج"""
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('products:product_list')
#     else:
#         form = ProductForm()
#     return render(request, 'products/add.html', {'form': form})

# def product_update(request, pk):
#     """تعديل منتج موجود بواسطة المفتاح الأساسي pk"""
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         form = ProductForm(request.POST, instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect('products:product_list')
#     else:
#         form = ProductForm(instance=product)
#     return render(request, 'products/edit.html', {'form': form, 'product': product})

# def product_delete(request, pk):
#     """حذف منتج موجود بعد التأكيد"""
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         product.delete()
#         return redirect('products:product_list')
#     return render(request, 'products/delete.html', {'product': product})


# ============================================================
# Class-Based Views الجديدة مع نظام الصلاحيات والحماية
# ============================================================

class ProductListView(LoginRequiredMixin, View):
    """
    عرض قائمة المنتجات - متاح لأي مستخدم مسجل دخوله
    LoginRequiredMixin: يحوّل المستخدم غير المسجل لصفحة تسجيل الدخول
    """
    template_name = 'products/list.html'

    def get(self, request):
        products = Product.objects.all()
        return render(request, self.template_name, {'products': products})


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """
    إضافة منتج جديد - يتطلب تسجيل الدخول + صلاحية (products.add_product)
    PermissionRequiredMixin: يرفض المستخدم الذي لا يملك الصلاحية برمز 403
    """
    template_name = 'products/add.html'
    permission_required = 'products.add_product'
    raise_exception = True  # إظهار 403 بدلاً من التحويل لصفحة تسجيل الدخول

    def get(self, request):
        form = ProductForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:product_list')
        return render(request, self.template_name, {'form': form})


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """
    تعديل منتج موجود - يتطلب تسجيل الدخول + صلاحية (products.change_product)
    """
    template_name = 'products/edit.html'
    permission_required = 'products.change_product'
    raise_exception = True

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(instance=product)
        return render(request, self.template_name, {'form': form, 'product': product})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:product_list')
        return render(request, self.template_name, {'form': form, 'product': product})


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """
    حذف منتج - يتطلب تسجيل الدخول + صلاحية (products.delete_product)
    GET: عرض صفحة تأكيد الحذف / POST: تنفيذ الحذف
    """
    template_name = 'products/delete.html'
    permission_required = 'products.delete_product'
    raise_exception = True

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, self.template_name, {'product': product})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return redirect('products:product_list')
