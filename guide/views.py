# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# from django.http import HttpResponse
from guide.models import Post,Category

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    category_list =Category.objects.all()
    return render(request, 'guide/index.html', context={'post_list':post_list,'category_list':category_list})
