from django.db import models

class Date(models.Model):
    reception_date = models.DateField(auto_now=True)
    deliver_date = models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return str(self.id)