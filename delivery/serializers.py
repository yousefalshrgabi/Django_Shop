from rest_framework import serializers
from .models import Delivery


class DeliverySerializer(serializers.ModelSerializer):
    """
    Serializer لتحويل نموذج Delivery إلى JSON والعكس.
    يُستخدم في API endpoints لعرض وإنشاء وتعديل بيانات سائقي التوصيل.

    الحقول المُضمَّنة:
        - id       : المفتاح الأساسي (للقراءة فقط)
        - name     : اسم السائق
        - email    : البريد الإلكتروني
        - phone    : رقم الهاتف
        - address  : العنوان
    """

    class Meta:
        model = Delivery
        fields = ['id', 'name', 'email', 'phone', 'address']
        read_only_fields = ['id']  # id لا يمكن تعديله

    def validate_phone(self, value):
        """
        التحقق من أن رقم الهاتف موجب
        """
        if value <= 0:
            raise serializers.ValidationError('رقم الهاتف يجب أن يكون رقماً موجباً.')
        return value

    def validate_name(self, value):
        """
        التحقق من أن الاسم ليس فارغاً
        """
        if not value.strip():
            raise serializers.ValidationError('الاسم لا يمكن أن يكون فارغاً.')
        return value.strip()
