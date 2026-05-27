from django.db import models

class Spacecraft(models.Model):
    
    class StatusChoices(models.TextChoices):
        PLANNING = 'проектируется', 'Проектируется'
        IN_TRANSIT = 'в пути', 'В пути'
        IN_ORBIT = 'на орбите Юпитера', 'На орбите Юпитера'
        COMPLETED = 'завершена', 'Завершена'
        FAILED = 'авария', 'Авария'
    
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=50)
    launch_date = models.DateField()
    power_watts = models.PositiveIntegerField()
    mass_kg = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.PLANNING)
    
    def __str__(self):
        return f"{self.name} ({self.country})"


class Target(models.Model):
    
    class TypeChoices(models.TextChoices):
        GALILEAN = 'галилеевы', 'Галилеевы'
        REGULAR = 'регулярные', 'Регулярные'
        IRREGULAR = 'иррегулярные', 'Иррегулярные'
    
    name = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=20, choices=TypeChoices.choices)
    diameter_km = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    gravity_ms2 = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    has_ocean = models.BooleanField(default=False)
    notable_feature = models.TextField(blank=True)
    
    def __str__(self):
        return self.name


class Mission(models.Model):
    
    class StatusChoices(models.TextChoices):
        PLANNING = 'планируется', 'Планируется'
        ACTIVE = 'активна', 'Активна'
        COMPLETED = 'завершена', 'Завершена'
        FAILED = 'неудача', 'Неудача'
    
    spacecraft = models.ForeignKey(Spacecraft, on_delete=models.RESTRICT)
    target = models.ForeignKey(Target, on_delete=models.RESTRICT)
    mission_name = models.CharField(max_length=100, unique=True)
    budget_usd = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.PLANNING)
    
    def __str__(self):
        return self.mission_name


class Instrument(models.Model):
    
    class TypeChoices(models.TextChoices):
        CAMERA = 'камера', 'Камера'
        SPECTROMETER = 'спектрометр', 'Спектрометр'
        MAGNETOMETER = 'магнитометр', 'Магнитометр'
        RADAR = 'радар', 'Радар'
        PLASMA = 'плазменный анализатор', 'Плазменный анализатор'
    
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=25, choices=TypeChoices.choices)
    mass_kg = models.DecimalField(max_digits=8, decimal_places=2)
    power_consumption_w = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"


class MissionInstrument(models.Model):
    
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    instrument = models.ForeignKey(Instrument, on_delete=models.RESTRICT)
    is_active = models.BooleanField(default=True)
    commissioning_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    
    class Meta:
        unique_together = ['mission', 'instrument']
    
    def __str__(self):
        return f"{self.mission.mission_name} → {self.instrument.name}"