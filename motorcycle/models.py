from django.db import models

class Motorcycle(models.Model):
    brand = models.TextField(max_length=100)
    line = models.TextField(max_length=100)
    def __str__(self):
        return self.brand +" : "+  self.line