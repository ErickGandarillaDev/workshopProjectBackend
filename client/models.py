from django.db import models

class Client(models.Model):
    name = models.TextField(max_length=100)
    phoneNumber = models.TextField(max_length=25)
    def __str__(self):
        return self.name