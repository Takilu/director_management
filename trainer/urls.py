from django.urls import path
from . import views

urlpatterns = [
    
   
    path('register', views.AdminView.as_view(), name= 'trainer_registration')
]
