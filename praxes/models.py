from django.db import models

# Create your models here.

class Name(models.Model):
    vorname = models.CharField(max_length=35, blank=True)
    nachname = models.CharField(max_length=35, blank=True)
    anmerkung = models.TextField(blank=True)

    def __str__(self):
        return self.nachname
