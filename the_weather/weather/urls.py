from django.conf.urls import url
from django.urls import path
from . import views

app_name='weather'

#Write your urls here
urlpatterns=[
    path('',views.index,name='index'),
]