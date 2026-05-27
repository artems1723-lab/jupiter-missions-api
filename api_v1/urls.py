from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SpacecraftViewSet, TargetViewSet, MissionViewSet,
    InstrumentViewSet, MissionInstrumentViewSet
)

router = DefaultRouter()
router.register(r'spacecraft', SpacecraftViewSet)
router.register(r'targets', TargetViewSet)
router.register(r'missions', MissionViewSet)
router.register(r'instruments', InstrumentViewSet)
router.register(r'mission-instruments', MissionInstrumentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]