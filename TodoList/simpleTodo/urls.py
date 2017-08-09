#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import *
from simpleTodo import views
# urlpatterns = patterns(('simpleTodo.views'),
#     url(r'^$', 'todolist', name='todo'),
#     url(r'^addtodo/$', 'addtodo', name='add'),
#     url(r'^todofinish/(?P<id>\d+)/$', 'todofinish', name='finish'),
#     url(r'^todobackout/(?P<id>\d+)/$', 'todoback',  name='backout'),
#     url(r'^updatetodo/(?P<id>\d+)/$', 'updatetodo', name='update'),
#     url(r'^tododelete/(?P<id>\d+)/$', 'tododelete', name='delete'),
# )
urlpatterns = patterns(('simpleTodo.views'),
    url(r'^$', 'todolist', name='todo'),
    url(r'^addtodo/$', views.addtodo, name='add'),
    url(r'^todofinish/(?P<id>\d+)/$', views.todofinish, name='finish'),
    url(r'^todobackout/(?P<id>\d+)/$', views.todoback,  name='backout'),
    url(r'^updatetodo/(?P<id>\d+)/$', views.updatetodo, name='update'),
    url(r'^tododelete/(?P<id>\d+)/$', views.tododelete, name='delete'),
)
