from django.shortcuts import render
from rest_framework import viewsets, renderers

from django.views import View 
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate

from rest_framework import permissions
#from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User

from . models import TrainingType, Trainer
from . serializers import TrainingTypeSerializer,CertifacteSerializer, UserSerializer
from . forms import RegisterTrainer



# views.py
from rest_framework import viewsets, filters
from .models import *
from .serializers import *

class TrainerAccountViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'email', 'firstName', 'lastName', 
        'phone_number', 'region'
    ]

class AdminAccountViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'email', 'firstName', 'lastName', 
        'phone_number', 'region'
    ]

class TrainingTypeViewSet(viewsets.ModelViewSet):
    queryset = TrainingType.objects.all()
    serializer_class = TrainingTypeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['training_id', 't_type']

class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['cont_id',
        'sign_by__firstName', 'for_training',
    ]

class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certifcate.objects.all()
    serializer_class = CertifacteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'cert_type', 'description', 
        'awarded_for__for_training__name_of_training'
    ]

class BusinessViewSet(viewsets.ModelViewSet):
    queryset= BusinessLicense.objects.all()
    serializer_class= BusinessLicenseSerializers
    filter_backends= [filters.SearchFilter]
    search_fields= [
        'TIN', 'owner'
    ]
