from django.db import models


class MortgageInfo(models.Model):
    cost = models.IntegerField()
    initial_fee = models.IntegerField()
    years = models.IntegerField()
