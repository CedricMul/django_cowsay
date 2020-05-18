from django.db import models

class CowUser(models.Model):
    say = models.CharField(max_length=120)
