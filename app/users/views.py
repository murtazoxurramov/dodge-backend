from django.contrib.auth import login, logout
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated

from app.users.serializers import CustomTokenObtainPairSerializer, PhoneNumberLoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class RefreshTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        refresh_token = RefreshToken.for_user(request.user)
        return Response({
            'access_token': str(refresh_token.access_token),
            'refresh_token': str(refresh_token),
        })


class PhoneNumberLoginView(generics.GenericAPIView):
    serializer_class = PhoneNumberLoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({'detail': 'Login successful'})

    # def delete(self, request):
    #     logout(request)
    #     return Response({'detail': 'Logout successful'})

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
