# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User)
    todo = models.CharField(max_length = 50) #打算做的任务
    flag = models.CharField(max_length = 2, default = '1')
    priority = models.CharField(max_length = 2, default ='0')
    pub_date = models.DateTimeField('publish-time',auto_now_add = True)
    
    def __unicode__(self):
        return u'%d %s %s' %(self.id, self.todo,self.flag)
     
    class Meta:
        # 模型按照 priority 和 pub_date 按升序排序
        ordering = ['priority', 'pub_date']
