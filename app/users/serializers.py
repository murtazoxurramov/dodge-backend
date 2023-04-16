from rest_framework import serializers
from .backend import PhoneNumberAuthentication
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['email'] = user.email
        return token


class PhoneNumberLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=12)
    password = serializers.CharField()

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')
        user = PhoneNumberAuthentication().authenticate(
            phone_number=phone_number, password=password)
        if not user:
            raise serializers.ValidationError(
                'Incorrect phone number or password')
        attrs['user'] = user
        return attrs


# class PhoneNumberLoginSerializer(serializers.Serializer):
#     phone_number = serializers.CharField(max_length=12)
#     password = serializers.CharField()

#     def validate(self, attrs):
#         phone_number = attrs.get('phone_number')
#         password = attrs.get('password')
#         user = PhoneNumberAuthentication().authenticate(
#             self.context['request'])
#         if not user or user.phone_number != phone_number:
#             raise serializers.ValidationError(
#                 'Incorrect phone number or password')
#         if not user.check_password(password):
#             raise serializers.ValidationError(
#                 'Incorrect phone number or password')
#         attrs['user'] = user
#         return attrs
