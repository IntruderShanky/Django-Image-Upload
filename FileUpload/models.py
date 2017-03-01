from __future__ import unicode_literals

from django.db import models


class Details(models.Model):
    image = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
