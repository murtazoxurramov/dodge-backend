from rest_framework import generics

class PhoneNumberLoginView(generics.GenericAPIView):
    serializer_class = PhoneNumberLoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({'detail': 'Login successful'})
