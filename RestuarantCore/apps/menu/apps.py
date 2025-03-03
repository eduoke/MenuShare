from django.apps import AppConfig


class MenuConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'RestuarantCore.apps.menu'
    verbose_name = 'Menu'
    
    def ready(self):
        import RestuarantCore.apps.menu.signals  # Import the signals module to connect the signal
