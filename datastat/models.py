"""
Models for Database
"""

from django.db import models

class ColorFrequency(models.Model):
    color = models.CharField(max_length=100)
    frequency = models.IntegerField()

    def __str__(self):
        return f"{self.color}: {self.frequency}"
