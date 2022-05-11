import imp
from django.urls import path
from formmodel_app import views

urlpatterns = [
    path('',views.user,name='user'),
]