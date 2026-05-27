from rest_framework import viewsets
from rest_framework_extensions.cache.decorators import cache_response
from .models import Spacecraft, Target, Mission, Instrument, MissionInstrument
from .serializers import (
    SpacecraftSerializer, TargetSerializer, MissionSerializer,
    InstrumentSerializer, MissionInstrumentSerializer
)


class SpacecraftViewSet(viewsets.ModelViewSet):
    serializer_class = SpacecraftSerializer
    queryset = Spacecraft.objects.all()
    
    @cache_response(60 * 15)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class TargetViewSet(viewsets.ModelViewSet):
    serializer_class = TargetSerializer
    queryset = Target.objects.all()
    
    @cache_response(60 * 15)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class MissionViewSet(viewsets.ModelViewSet):
    serializer_class = MissionSerializer
    queryset = Mission.objects.all()
    
    @cache_response(60 * 15)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class InstrumentViewSet(viewsets.ModelViewSet):
    serializer_class = InstrumentSerializer
    queryset = Instrument.objects.all()
    
    @cache_response(60 * 15)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class MissionInstrumentViewSet(viewsets.ModelViewSet):
    serializer_class = MissionInstrumentSerializer
    queryset = MissionInstrument.objects.all()
    
    @cache_response(60 * 15)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)