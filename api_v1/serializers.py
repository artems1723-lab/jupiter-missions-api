from rest_framework import serializers
from .models import Spacecraft, Target, Mission, Instrument, MissionInstrument


class SpacecraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spacecraft
        fields = ['id', 'name', 'country', 'launch_date', 'power_watts', 'mass_kg', 'status']


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['id', 'name', 'type', 'diameter_km', 'gravity_ms2', 'has_ocean', 'notable_feature']


class MissionSerializer(serializers.ModelSerializer):
    spacecraft = SpacecraftSerializer(read_only=True)
    target = TargetSerializer(read_only=True)
    
    spacecraft_id = serializers.PrimaryKeyRelatedField(
        queryset=Spacecraft.objects.all(), source='spacecraft', write_only=True
    )
    target_id = serializers.PrimaryKeyRelatedField(
        queryset=Target.objects.all(), source='target', write_only=True
    )
    
    class Meta:
        model = Mission
        fields = [
            'id', 'mission_name', 'spacecraft', 'spacecraft_id',
            'target', 'target_id', 'budget_usd', 'start_date',
            'end_date', 'status'
        ]


class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = ['id', 'name', 'type', 'mass_kg', 'power_consumption_w', 'description']


class MissionInstrumentSerializer(serializers.ModelSerializer):
    mission = MissionSerializer(read_only=True)
    instrument = InstrumentSerializer(read_only=True)
    
    mission_id = serializers.PrimaryKeyRelatedField(
        queryset=Mission.objects.all(), source='mission', write_only=True
    )
    instrument_id = serializers.PrimaryKeyRelatedField(
        queryset=Instrument.objects.all(), source='instrument', write_only=True
    )
    
    class Meta:
        model = MissionInstrument
        fields = ['id', 'mission', 'mission_id', 'instrument', 'instrument_id', 
                  'is_active', 'commissioning_date', 'notes']