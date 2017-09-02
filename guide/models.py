# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=10)
    def __unicode__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=30)
    url = models.CharField(max_length=100)
    iconurl = models.CharField(max_length=100)
    body = models.TextField()
    tag = models.ForeignKey(Category)
    created_time = models.DateTimeField()
    author = models.CharField(max_length=10)
    def __unicode__(self):
        return self.title
