from django.db import models
from Hackvoting import settings
# Create your models here.

class Hacker(models.Model):
    Name = models.CharField(unique=True,max_length=200)
    code = models.IntegerField(unique=True)
    no_challenges = models.IntegerField()
    except_level = models.IntegerField()
    Data_structures = models.IntegerField()
    Algo = models.IntegerField()
    cpp = models.IntegerField()
    java = models.IntegerField()
    python = models.IntegerField()
    votes = models.IntegerField()