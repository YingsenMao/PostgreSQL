from django.db import models

# Create your models here.

class Babynames2(models.Model):
    year = models.FloatField(blank=True, null=True)
    sex = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    n = models.IntegerField(blank=True, null=True)
    prop = models.FloatField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'babynames2'