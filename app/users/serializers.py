from rest_framework import serializers

class PhoneNumberLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=12)
    password = serializers.CharField()

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')
        user = authenticate(phone_number=phone_number, password=password)
        if not user:
            raise serializers.ValidationError('Incorrect phone number or password')
        attrs['user'] = user
        return attrs