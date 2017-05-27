# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import  Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('user', 'todo','priority','flag','pub_date',)
    # 这个字段元组创建过滤器，它位于列表页面的右边。Django为日期型字段提供了快捷过滤方式,它包含:今天、过往七天、当月和今年。这些是开发人员经常用到的。
    list_filter =('pub_date',)  
    # 按pub_date降序
    ordering = ('-pub_date',) 
    
admin.site.register(Todo,TodoAdmin)  # 如果没有第二个参数则默认使用对象中的__unicode__()方法进行显示
    
