from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import AccountViewSet

router = routers.DefaultRouter()
router.register(r'account', AccountViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
