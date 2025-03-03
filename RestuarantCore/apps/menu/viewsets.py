from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Menu

from .serializer import MenuSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all() 
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        # Attach the request object to the instance
        menu = serializer.save()
        menu._request = self.request  # Pass the request object to the instance
        menu.save()  # Save the instance (the signal will handle setting the user)

