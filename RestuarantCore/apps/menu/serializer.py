from rest_framework import serializers 
from .models import Menu 


class MenuSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Menu 
        fields = [
            'name',
            'price',
            'created',
            'updated',
            'id',
            'get_username'
        ]
        read_only_fields = ['created', 'updated', 'id', 'get_username']
        
        