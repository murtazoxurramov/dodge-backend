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


class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'profile_image',
                  'phone_number', 'email', 'password']

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.profile_image = validated_data.get(
            'profile_image', instance.profile_image)
        instance.phone_number = validated_data.get(
            'phone_number', instance.phone_number)
        instance.email = validated_data.get(
            'email', instance.email)
        instance.password = validated_data.get(
            'password', instance.password)
        instance.save()
        return instance
