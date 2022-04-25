from django.db import models

class Feladat(models.Model):

    nev=models.CharField(primary_key=True,max_length=100,blank=False)
    resztvevo=models.CharField(max_length=100,blank=True)

    class Meta:
     
        verbose_name = 'Feladat'
        verbose_name_plural = 'Feladats'

    def __str__(self):
        return self.nev
