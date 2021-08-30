from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from form_demo import views 

urlpatterns = [
   path('name',views.get_name,name="name")
]