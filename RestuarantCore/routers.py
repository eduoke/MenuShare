from rest_framework import routers

from RestuarantCore.apps.menu.viewsets import MenuViewSet
from RestuarantCore.apps.users.viewsets import UserViewSet

router = routers.DefaultRouter()

router.register(r'menu', MenuViewSet)
router.register(r'users', UserViewSet)

urlpatterns = router.urls