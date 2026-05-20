from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    """
    نموذج تسجيل مستخدم جديد - يمتد من UserCreationForm المدمج في Django
    يضيف حقل البريد الإلكتروني مع تخصيص الـ widgets
    """
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'البريد الإلكتروني',
            'id': 'id_email'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'اسم المستخدم',
            'id': 'id_username'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'كلمة المرور',
            'id': 'id_password1'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'تأكيد كلمة المرور',
            'id': 'id_password2'
        })


class LoginForm(AuthenticationForm):
    """
    نموذج تسجيل الدخول - يمتد من AuthenticationForm المدمج في Django
    يتحقق من صحة اسم المستخدم وكلمة المرور تلقائياً
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'اسم المستخدم',
            'id': 'id_login_username'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'كلمة المرور',
            'id': 'id_login_password'
        })
