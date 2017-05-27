"""my_todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from  todoapp import views as todoapp_views
urlpatterns = [
    url(r'^$', todoapp_views.todolist, name= 'todo'),
    url(r'^todofinish/(?P<id>\d+)/$', todoapp_views.todofinish, name = 'finish'),
    url(r'^todobackout/(?P<id>\d+)/$', todoapp_views.todoback,name = 'backout'),
    url(r'^tododelete/(?P<id>\d+)/$', todoapp_views.tododelete, name = 'delete'),
    url(r'^addtodo/$', todoapp_views.addTodo, name = 'add'),
    url(r'^updatetodo/(?P<id>\d+)/$', todoapp_views.updatetodo, name = 'update'),
    url(r'^admin/', admin.site.urls),
]
