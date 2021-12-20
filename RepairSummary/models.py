from django.db import models
from diagnosis.models import Diagnosis
from date.models import Date
from client.models import Client
from status.models import Status
from motorcycle.models import Motorcycle

from django.conf import settings


class RepairSummary(models.Model):
    initialInfo = models.CharField(max_length=100)
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.DO_NOTHING)
    date = models.ForeignKey(Date, on_delete=models.DO_NOTHING)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    motorcycle = models.ForeignKey(Motorcycle, on_delete=models.DO_NOTHING)
    
    
    def __str__(self):
        return self.initialInfo
