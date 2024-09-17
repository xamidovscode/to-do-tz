import re
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    @classmethod
    def validate_phone(cls, value):
        phone_regex = re.compile(r'^\+998\d{9}$')
        if not phone_regex.match(value):
            raise serializers.ValidationError("Phone is not valid")
        return value

    def validate(self, attrs):
        password = attrs['password']
        user = self.context['user']
        if not user:
            raise serializers.ValidationError({'phone': "User not found"})
        if not user.check_password(password):
            raise serializers.ValidationError({'password': "The password is incorrect"})
        return attrs