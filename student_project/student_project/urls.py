"""student_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from studentrecords import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'base',views.index,name="base"),
    url(r'admin/', admin.site.urls,name="admin"),
    url(r'stud', views.stud, name = 'stud'),
    url(r'show',views.show, name = 'show'),
    url(r'searchpage',views.searchpage, name = 'searchpage'),
    url(r'search/', views.search, name = "search"),
    path('edit/<int:Reg_no>', views.edit),
    path('update/<int:Reg_no>', views.update),
    path('delete/<int:Reg_no>', views.destroy),
]
