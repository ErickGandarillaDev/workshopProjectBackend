from django.db import models

class Status(models.Model):
    description = models.TextField(max_length=100)
    def __str__(self):
        return self.description 