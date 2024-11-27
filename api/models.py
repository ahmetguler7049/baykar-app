from django.db import models
from django.utils import timezone


class Aircraft(models.Model):
    AIRCRAFT_CHOICES = [
        ('TB2', 'TB2'),
        ('TB3', 'TB3'),
        ('Akıncı', 'Akıncı'),
        ('Kızıl Elma', 'Kızıl Elma'),
    ]
    name = models.CharField(max_length=100, choices=AIRCRAFT_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    TEAM_CHOICES = [
        ('Kanat', 'Kanat'),
        ('Gövde', 'Gövde'),
        ('Kuyruk', 'Kuyruk'),
        ('Aviyonik', 'Aviyonik'),
        ('Montaj', 'Montaj'),
    ]

    name = models.CharField(max_length=100, choices=TEAM_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name


class Part(models.Model):
    aircraft = models.ForeignKey(Aircraft, related_name="parts", on_delete=models.CASCADE)
    team = models.ForeignKey(Team, related_name="parts", on_delete=models.CASCADE)

    @property
    def name(self):
        return f"{self.aircraft.name} - {self.team.name}"

    def __str__(self):
        return self.name


class AircraftInventory(models.Model):
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, related_name="aircraft_inventories", on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, blank=True, verbose_name="Oluşturma Tarihi")

    @property
    def name(self):
        return self.aircraft.name

    def __str__(self):
        return self.name


class PartInventory(models.Model):
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    aircraft_inventory = models.ForeignKey(AircraftInventory, related_name="part_inventories", on_delete=models.CASCADE)

    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now, blank=True, verbose_name="Oluşturma Tarihi")
    used_at = models.DateTimeField(blank=True, null=True, verbose_name="Kullanım Tarihi")

    @property
    def name(self):
        return self.part.name

    def save(self, *args, **kwargs):
        if self.used_at:
            self.is_used = True
        super(PartInventory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
