from django.db import models

class Airport(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

class FlightPath(models.Model):
    source = models.ForeignKey(Airport, related_name='departures', on_delete=models.CASCADE)
    destination = models.ForeignKey(Airport, related_name='arrivals', on_delete=models.CASCADE)
    distance = models.FloatField()

    def __str__(self):
        return f"{self.source} → {self.destination} ({self.distance} km)"


# Create your models here.
