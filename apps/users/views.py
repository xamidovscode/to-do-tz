from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from . import serializers
from rest_framework.response import Response
from .models import User


class LoginView(generics.CreateAPIView):
    serializer_class = serializers.LoginSerializer

    def create(self, request, *args, **kwargs):
        user = User.objects.filter(phone=request.data.get("phone")).first()
        serializer = self.serializer_class(data=request.data, context={"user": user})
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        data['tokens'] = user.tokens()
        return Response(data, status=status.HTTP_200_OK)


