from datetime import timedelta

from django.utils import timezone
from rest_framework import status, views
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    UserSignInSerializer,
    UserEditSerializer
)


class UserRegistrationView(GenericAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user_id': user.pk,
            'phone_number': user.phone_number,
            'email': user.email
        }, status=status.HTTP_201_CREATED)


class UserLoginView(GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id = serializer.validated_data['user_id']
        user = User.objects.get(pk=user_id)
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user_id': user_id
        })


# class UserSignInView(GenericAPIView):
#     serializer_class = UserSignInSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         phone_number = serializer.validated_data['phone_number']
#         code = serializer.validated_data['code']

#         try:
#             user = User.objects.get(phone_number=phone_number)
#         except User.DoesNotExist:
#             raise ValidationError({'phone_number': ['User does not exist.']})

#         if not user.last_login_code or user.last_login_code != code:
#             raise ValidationError({'code': ['Invalid code.']})

#         if user.last_login_code_time < timezone.now() - timedelta(minutes=5):
#             raise ValidationError({'code': ['Code has expired.']})

#         user.last_login_code = None
#         user.last_login_code_time = None
#         user.save()

#         return Response({'token': user.auth_token.key})

class UserLogoutView(views.APIView):
    """
    Logout view to invalidate the current user's token.
    """

    def post(self, request, *args, **kwargs):
        # Delete the user's auth token to log them out.
        request.user.auth_token.delete()
        return Response({'message': 'User has been logged out.'}, status=status.HTTP_200_OK)


class UserEditView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserEditSerializer
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user
