from rest_framework import serializers
from . models import Admin, Trainer,TrainingType,Certifcate, Contract, BusinessLicense
from django.contrib.auth.models import User


 
class AdminSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =Admin
        fields= ['email', 'firstName', 'lastName','phone_number']

class TrainerSerializer(serializers.ModelSerializer):

    class Meta:
        model= Trainer
        fields= ['id','email', 'firstName', 'lastName','phone_number', 'ownBussiness','business_tin','assigned_for']


class TrainingTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model=TrainingType
        fields =  ['training_id','t_type','description', 'start_date','owner']
    
 
class CertifacteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Certifcate
        fields= '__all__'

class ContractSerializer(serializers.ModelSerializer):
    # signed_by= serializers.CharField(source= 'Trainer.email')
    class Meta:
        model =Contract
        fields= '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class BusinessLicenseSerializers(serializers.ModelSerializer):
    class Meta:
        model= BusinessLicense
        fields='__all__'