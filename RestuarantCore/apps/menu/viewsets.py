from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny,    IsAuthenticated
from .models import Menu

from .serializers import MenuSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all() 
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

