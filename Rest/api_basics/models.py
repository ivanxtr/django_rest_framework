# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  date = models.DateField(auto_now_add=True)

# return a human-readable format
  def __str__(self):
    return self.title
