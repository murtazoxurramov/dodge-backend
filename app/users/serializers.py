from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['phone_number', 'email', 'password']

    def create(self, validated_data):
        user = User(
            phone_number=validated_data['phone_number'],
            email=validated_data.get('email')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserLoginSerializer(TokenObtainPairSerializer):
    phone_number = serializers.CharField(required=True)

    def validate(self, attrs):
        data = super().validate(attrs)
        user = User.objects.get(phone_number=attrs['phone_number'])
        data['user_id'] = user.pk
        return data


class UserSignInSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True)
    code = serializers.CharField(required=True)
