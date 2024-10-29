"""
URL configuration for camila_diaz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home' ),
    path('home/', views.home, name='home' ),
    # Characters URLs
    path('char/', views.char_list, name='char_list'),
    path('char/<int:pk>/', views.char_detail, name='char_detail'),
    path('char/new/', views.char_new, name='char_new'),
    path('char/<int:pk>/edit/', views.char_edit, name='char_edit'),
    path('char/delete/<int:pk>/', views.char_delete, name='char_delete'),
    
    # Classes URLs
    path('class/', views.class_list, name='class_list'),
    path('class/<int:pk>/', views.class_detail, name='class_detail'),
    path('class/new/', views.class_new, name='class_new'),
    path('class/<int:pk>/edit/', views.class_edit, name='class_edit'),
    path('class/delete/<int:pk>/', views.class_delete, name='class_delete'),
    
    # Spells URLs 
    path('spell/', views.spell_list, name='spell_list'),
    path('spell/<int:pk>/', views.spell_detail, name='spell_detail'),
    path('spell/new/', views.spell_new, name='spell_new'),
    path('spell/<int:pk>/edit/', views.spell_edit, name='spell_edit'),
    path('spell/delete/<int:pk>/', views.spell_delete, name='spell_delete'),
    
    # Traits URLs
    path('trait/', views.trait_list, name='trait_list'),
    path('trait/<int:pk>/', views.trait_detail, name='trait_detail'),
    path('trait/new/', views.trait_new, name='trait_new'),
    path('trait/<int:pk>/edit/', views.trait_edit, name='trait_edit'),
    path('trait/delete/<int:pk>/', views.trait_delete, name='trait_delete'),
]
