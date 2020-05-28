#\learning_logs\urls.py
'''define the url patterns of learning_logs'''
from django.conf.urls import url

from . import views

app_name = 'learning_logs'
urlpatterns=[
    #mainpage
    url(r'^$', views.index, name='index'),
    
    #show all topics
    url(r'^topics/$',views.topics,name='topics'),
    
    #details of specific topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    
    #page used to add new topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    
    #page used to add new entry
    url(r'^new_enry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    
    #page used to edit entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),

    ]
