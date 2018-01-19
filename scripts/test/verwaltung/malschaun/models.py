from django.db import models

# Create your models here.


class Schue(models.Model):
    n = models.IntegerField()
    nachname = models.CharField(max_length=1)
    vorname = models.CharField(max_length=1)
    rname = models.CharField(max_length=1,default="a")
#    klasse = models.ForeignKey(Klasse, default="klasse")
    jg = models.IntegerField(null=True)
    schuljahr = models.CharField(max_length=5)
#    kurse = models.ManyToManyField(Kurs, through='SchuelerKurs')



class ASchue(models.Model):
    n = models.IntegerField()
    nachname = models.CharField(max_length=1)
    vorname = models.CharField(max_length=1)
    orname = models.CharField(max_length=1,default="a")
#    klasse = models.ForeignKey(Klasse, default="klasse")
    jg = models.IntegerField(null=True)
    schuljahr = models.CharField(max_length=5)
#    kurse = models.ManyToManyField(Kurs, through='SchuelerKurs')
