from django.db import models

class Schedule(models.Model):
    fan_start = models.DecimalField(max_digits=3, decimal_places=1)
    fan_stop = models.DecimalField(max_digits=3, decimal_places=1)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()

    def __str__(self):
        return f"Schedule - Fan Start: {self.fan_start}, Fan Stop: {self.fan_stop}, Start At: {self.start_at}, End At: {self.end_at}"
class Temp(models.Model):
    temperature = models.DecimalField(max_digits=3, decimal_places=1)
    def __str__(self):
        return f"Schedule - Temp: {self.temperature}"

# Create your models here.
