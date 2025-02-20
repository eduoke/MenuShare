import re
from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _



class MenuManager(models.Manager):
    
    def new_menu(self, name):
        new_menu = self.create(name=re.sub('\s+', '-', name).lower())
        
        new_menu.save()
        return new_menu


class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.name = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name=_('User'), 
        on_delete=models.CASCADE,
        # default=get_user(kwargs.pop('request').user.is_anonymous)
    )
    
    objects = MenuManager()
    
    class Meta:
        verbose_name = _('Menu')
        verbose_name_plural = _('Menus')
        
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Import get_user to access the logged-in user
        from django.contrib.auth import get_user
        # Get the logged-in user from the request
        user = get_user(kwargs.pop('request').user)
        self.user = user # Set the user field 
        if not self.user.is_authenticated:
            self.user['default'] = user.is_anonymous
            
        super().save(*args, **kwargs) # Call the parent save method
