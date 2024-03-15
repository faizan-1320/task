from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer,LoginSerializer,UpdateSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout
from .models import User

# Create your views here.
class RegiserView(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Register Succesfully!'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        print('Request data:', request.data)
        
        if serializer.is_valid(raise_exception=True):
            email = request.data.get('email')
            password = request.data.get('password')
            print('Email:', email)
            print('Password:', password)
            
            user = User.objects.get(email=email)
            print('Authenticated user:', user)
            
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key,'email':user.email,'id':user.id})
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UpdateSerializer
