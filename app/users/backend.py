from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication


class PhoneNumberAuthentication(BaseAuthentication):
    def authenticate(self, request):
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(phone_number=phone_number)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return (user, None)
        return None
