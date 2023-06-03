from django.db import models

# Create your models here.


class PilsDetail(models.Model):
    name = models.CharField(max_length=200)
    cond = models.IntegerField()




class SalesDetails(models.Model):
    patient_name = models.CharField(max_length=200)
    pils_name = models.ForeignKey(PilsDetail, on_delete=models.PROTECT)
    sale_date = models.DateField()
