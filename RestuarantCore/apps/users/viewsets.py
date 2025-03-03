from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets 
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializer import NewUserRegistrationSerializer, UserSerializer

# Get the UserModel 
UserModel = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    
class LogoutViewSet(viewsets.ModelViewSet):
    ... 
    
