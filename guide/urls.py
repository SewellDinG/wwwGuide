#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from guide import views

urlpatterns = [
    url(r'^$', views.index),
]
