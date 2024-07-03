from django.urls import path, include
from .views import HududViewSet,QurilishTashkilotiViewSet, QurilishBinoViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('hudud', HududViewSet)
router.register('tashkilot', QurilishTashkilotiViewSet)
router.register('bino', QurilishBinoViewSet)


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),

    path('api/v1/', include(router.urls)),
]