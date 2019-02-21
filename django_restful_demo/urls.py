"""django_restful_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from day01.views import Users
from day02.views import TestView02
from day03.views import TestView03
from day03_1.views import TestView03_1
from day04.views import TestView04
from day05.views import TestView05
from day06.views import TestView06
from day06_1.views import TestView06_1
from day07.views import AuthView, OrderView, UserInfoView
from day08.views import TestView08

urlpatterns = [
    path('users/', Users.as_view()),
    path('test02/', TestView02.as_view()),
    path('test03/', TestView03.as_view()),
    path('test03_1/', TestView03_1.as_view()),
    path('test04/', TestView04.as_view()),
    path('test05/', TestView05.as_view()),
    path('test06/', TestView06.as_view()),
    path('test06_1/', TestView06_1.as_view()),
    path('api/v1/auth/', AuthView.as_view()),
    path('api/v1/order/', OrderView.as_view()),
    path('api/v1/info/', UserInfoView.as_view()),
    path('test08/', TestView08.as_view()),
    path('admin/', admin.site.urls),
]
