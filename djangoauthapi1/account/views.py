from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from account.seralizers import UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth import authenticate

class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"msg": "User registration successful!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self,request, format=None):
        seralizer = UserLoginSerializer(data=request.data)
        if seralizer.is_valid(raise_exception=True):
            email = seralizer.data.get('email')
            password = seralizer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is None:
                return Response({"msg": "login successful"}, status=status.HTTP_200_OK)
            else:
                return Response({'errors':{"non_field_errors": ["Email or Password is not valid"]}}, status=status.HTTP_404_UNAUTHORIZED)
        return Response(seralizer.errors, status=status.HTTP_400_BAD_REQUEST)
        
       