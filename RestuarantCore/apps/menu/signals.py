from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Menu

@receiver(pre_save, sender=Menu)
def set_menu_user(sender, instance, **kwargs):
    if not instance.user_id:  # Check if the user field is not already set
        request = getattr(instance, '_request', None)  # Get the request object from the instance
        if request and request.user.is_authenticated:  # Ensure the user is logged in
            instance.user = request.user  # Set the user field