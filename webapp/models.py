from django.db import models

class Schedule(models.Model):
    fan_start = models.DecimalField(max_digits=3, decimal_places=1)
    fan_stop = models.DecimalField(max_digits=3, decimal_places=1)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()

    def __str__(self):
        return f"Schedule - Fan Start: {self.fan_start}, Fan Stop: {self.fan_stop}, Start At: {self.start_at}, End At: {self.end_at}"

class Greenhouse(models.Model):
    temp = models.DecimalField(max_digits=3, decimal_places=1)
    humid = models.DecimalField(max_digits=5, decimal_places=2)
    moist = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return f"Greenhouse - Temperature: {self.temp}, Humidity: {self.humid}, Moisture: {self.moist}"

# Create your models here.
