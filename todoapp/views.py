# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import Http404
from django.contrib.auth.models import User
from todoapp.models import Todo
# Create your views here.
def todolist(request):   # 打算做的所有清单
    todolist = Todo.objects.filter(flag='1') # 还没有完成的todolist（flag=1）
    finishtodos = Todo.objects.filter(flag='0')
    return render(request, 'simpleTodo.html',
        {'todolist': todolist,'finishtodos': finishtodos})
        
def todofinish(request, id):
    todo = Todo.objects.get(id =str(id))
    if todo.flag == '1':
        todo.flag = '0'
        todo.save()
        return HttpResponseRedirect('/')
    todolist = Todo.objects.filter(flag = 1)
    return render(request, 'simpleTodo.html', {'todolist': todolist})
    
def todoback(request, id=''):   # 将已完成的任务撤回
    todo = Todo.objects.get(id = id)
    if todo.flag == '0':
        todo.flag = '1'
        todo.save()
        return HttpResponseRedirect('/')
    todolist = Todo.objects.filter(flag = 1)
    return render(request, 'simpleTodo.html',{'todolist': todolist})
    
def tododelete(request, id = ''):     # 删除选定id的任务
    try:
        todo = Todo.objects.get(id = id)
    except Exception: # 缺省情况下，异常类都继承自 Exception
        raise Http404
    if todo:
        todo.delete()  # 删除该对象
        return HttpResponseRedirect('/')
    todolist = Todo.objects.filter(flag = 1)
    return render(request, 'simpleTodo.html', {'todolist': todolist})

def addTodo(request):   # 添加 todo事项
    if request.method == 'POST':
        atodo = request.POST['todo']
        priority = request.POST['priority']
        user = User.objects.get(id = '1')
        todo = Todo(user = user, todo = atodo, priority = priority, flag = '1')
        todo.save()
        todolist = Todo.objects.filter(flag = 1)
        finishtodos = Todo.objects.filter(flag = 0)
        return render(request, 'showtodo.html',{'todolist': todolist, 'finishodos': finishtodos})
    else:   # 如果没有POST:
        todolist = Todo.objects.filter(flag= 1)
        finishtodos = Todo.objects.filter(flag = 0)
        return render(request, 'simpleTodo.html',{'todolist': todolist, 'finishodos': finishtodos})
        
def updatetodo(request, id=''):  # 修改事项,  该函数有问题,目前未发现bug
    if request.method == 'POST':
        print ' todolist update   !'
        atodo = request.POST['todo']
        priority = request.POST['priority']
        user = User.objects.get(id = '1')
        todo = Todo(user = user, todo= atodo, priority =  priority, flag = '1')
        todo.save()
        todolist = Todo.objects.filter(flag = 1)
        finishtodos = Todo.objects.filter(flag = 0)
        return render(request, 'simpleTodo.html', {'todolist': todolist, 'finishtodos': finishtodos})
    else:
        try:
            todo = Todo.objects.get(id = id)
        except Exception:
            raise Http404
        return render(request, 'updatetodo.html', {'toto': todo})
        

                 
    
    
        
        
    

