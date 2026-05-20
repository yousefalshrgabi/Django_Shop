from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views import View
from django.contrib import messages
from .forms import RegisterForm, LoginForm


# ============================================================
# Class-Based Views للمصادقة (Authentication CBVs)
# ============================================================

class HomeView(View):
    """
    CBV للصفحة الرئيسية - متاحة للجميع بدون تسجيل دخول
    لا تحتوي على Navbar كامل، فقط زر تسجيل الدخول في الأعلى
    """
    template_name = 'accounts/home.html'

    def get(self, request):
        return render(request, self.template_name)


class RegisterView(View):
    """
    CBV لتسجيل مستخدم جديد
    GET  → عرض نموذج التسجيل
    POST → معالجة النموذج وحفظ المستخدم
    ⚠️ مقيّد: فقط المستخدم 'y' يستطيع إنشاء حسابات جديدة
    """
    template_name = 'accounts/register.html'
    form_class = RegisterForm

    def _check_permission(self, request):
        """
        التحقق من أن المستخدم الحالي هو 'y' أو superuser.
        يعيد True إذا مُسموح، False إذا ممنوع.
        """
        if not request.user.is_authenticated:
            messages.error(request, 'يجب تسجيل الدخول أولاً لإنشاء حسابات جديدة.')
            return False
        if request.user.username != 'y' and not request.user.is_superuser:
            messages.error(request, '⛔ غير مسموح. فقط المستخدم المدير يستطيع إنشاء حسابات جديدة.')
            return False
        return True

    def get(self, request):
        # التحقق من الصلاحية
        if not self._check_permission(request):
            return redirect('accounts:login')
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        # التحقق من الصلاحية
        if not self._check_permission(request):
            return redirect('accounts:login')
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'✅ تم إنشاء حساب "{user.username}" بنجاح.')
            # لا نسجل دخول المستخدم الجديد تلقائياً (لأن 'y' هو من أنشأ الحساب)
            return redirect('products:product_list')
        return render(request, self.template_name, {'form': form})


class UserLoginView(View):
    """
    CBV لتسجيل الدخول
    GET  → عرض نموذج تسجيل الدخول
    POST → التحقق من بيانات المستخدم وتسجيل الدخول
    """
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def get(self, request):
        # إذا كان المستخدم مسجلاً دخوله، حوِّله للصفحة الرئيسية
        if request.user.is_authenticated:
            return redirect('products:product_list')
        form = self.form_class(request)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'مرحباً {user.username}! تم تسجيل دخولك بنجاح.')
            # توجيه المستخدم للصفحة التي كان يحاول الوصول إليها
            next_url = request.GET.get('next', 'products:product_list')
            return redirect(next_url)
        messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة.')
        return render(request, self.template_name, {'form': form})


class UserLogoutView(View):
    """
    CBV لتسجيل الخروج
    POST → تسجيل خروج المستخدم وتوجيهه لصفحة تسجيل الدخول
    """
    def post(self, request):
        logout(request)
        messages.info(request, 'تم تسجيل خروجك بنجاح.')
        return redirect('accounts:login')

    def get(self, request):
        # السماح بـ GET أيضاً لسهولة الاستخدام
        logout(request)
        messages.info(request, 'تم تسجيل خروجك بنجاح.')
        return redirect('accounts:login')
