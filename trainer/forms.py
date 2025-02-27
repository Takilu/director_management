from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Trainer, TrainingType


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class TrainingTypeForm(forms.ModelForm):
    class Meta:
        model = TrainingType
        fields = ["training_id",'t_type', "description"]

class RegisterTrainer(UserCreationForm):
    
    @classmethod
    def get_extra_actions(cls):
        return []
    email= forms.EmailField(required=True)

    class Meta:
        model= Trainer
        fields= ['firstName','lastName', 'email','phone_number','password', 'sex','educationLevel', 'assigned_for']
