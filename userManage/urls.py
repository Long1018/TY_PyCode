# -*- coding: utf-8 -*-

from django.urls import path
from userManage import views

urlpatterns = [

    path(r'login/', views.UserLogin),
    path(r'register/', views.UserRegister),

]
