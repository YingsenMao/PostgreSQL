from django.db import models

# Create your models here.
class Babynames(models.Model):
    year = models.IntegerField(blank=True, null=True)
    sex = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    n = models.IntegerField(blank=True, null=True)
    prop = models.FloatField(blank=True, null=True)
    name_id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'babynames'