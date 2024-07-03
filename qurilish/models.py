from django.db import models
from django.contrib.auth.models import User

class Hudud(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class QurilishTashkiloti(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    xistore = models.CharField(max_length=100)
    hudud = models.ForeignKey(Hudud, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class QurilishBino(models.Model):
    name = models.CharField(max_length=100)
    maydonni = models.CharField(max_length=100)
    qavat = models.PositiveIntegerField()
    hudud = models.ForeignKey(Hudud, on_delete=models.CASCADE)
    qurilish_tashkilot = models.ForeignKey(QurilishTashkiloti, on_delete=models.CASCADE)
    parkovka = models.BooleanField(default=True)
    bolalar_maydoni = models.BooleanField(default=True)
    lift = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
