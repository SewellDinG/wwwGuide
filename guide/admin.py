# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post,Category

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'tag', 'author', 'created_time']

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
