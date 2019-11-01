"""Two_Table URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import path,include

from Crud import views

app_name = 'Crud'

urlpatterns = [
 
  path('login/', views.user_login, name='login'),
  path('logout/', views.user_logout, name='logout'),

  path('view', views.Ministry_list, name='Ministry_list'),
  path('new', views.Ministry_create, name='Ministry_new'),
  path('edit/<int:pk>', views.Ministry_update, name='Ministry_edit'),
  path('delete/<int:pk>', views.Ministry_delete, name='Ministry_delete'),

  path('viewGovernemt', views.GovernmentEmployee_list, name='GovernmentEmployee_list'),
  path('addGovernment', views.GovernmentEmployee_create, name='GovernmentEmployee_new'),
  path('editGovernment/<int:pk>', views.GovernmentEmployee_update, name='GovernmentEmployee_edit'),
  path('deleteGovernment/<int:pk>', views.GovernmentEmployee_delete, name='GovernmentEmployee_delete'),
]