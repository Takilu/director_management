from django.db import models
import random, uuid

from django.contrib.auth.models import User


random_id= random.randint(1,1000000)

class Account(models.Model):
    id= models.UUIDField(primary_key= True,default=random_id ,editable = False)
    email= models.EmailField(blank=False, null=False, primary_key=False,max_length=30)
    firstName= models.CharField(blank= False, null=False, max_length=30)
    lastName= models.CharField(blank=False, null=False, max_length=30)
    phone_number= models.PositiveIntegerField(null=True, blank=True)
    password= models.CharField(null=False, blank = True, default='password1234')
    created_date= models.DateField(auto_now_add=True)
    

    class Meta:
        abstract=True
        ordering =['-created_date']

class TrainingType(models.Model):
    training_id= models.CharField(blank=False, null=False, primary_key=True, max_length=30)
    t_type= models.CharField(blank=True, null=False, max_length=60)
    start_date= models.DateField(null=True)
    #given_by= models.CharField(blank=False, null=False, max_length=30)
    description= models.TextField(max_length=1000)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    #launched_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    class Meta:
        unique_together= ''


class BusinessLicense(models.Model):
    TIN= models.PositiveIntegerField(primary_key=True, null=False)
    #owner= models.ForeignKey(Trainer, on_delete=models.CASCADE)
    given_date= models.DateField()
    expired_date= models.DateField()

class Trainer(Account):
    age = models.PositiveIntegerField(default=18)
    sex = models.CharField(blank=False, null=False, max_length=10)
    region = models.CharField(blank=False, null=False, max_length=10)
    educationLevel = models.CharField(default="basic learning", max_length=30)
    #trainer_level=models.Choices(value='Non_EMPRETEC')
    amharic = models.BooleanField(default=True)
    afaan_oromo= models.BooleanField(default=False)
    tigrigna = models.BooleanField(default=False)
    sidamegna = models.BooleanField(default= False)
    ownBussiness= models.BooleanField(default=False)
    business_tin= models.ForeignKey(BusinessLicense, on_delete= models.SET_NULL, null=True)
    assigned_for=models.ForeignKey(TrainingType, on_delete=models.CASCADE, null=True)
    #level_of_certification = models.ForeignKey(Certifcate, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstName
    


class Certifcate(models.Model):
    cert_id = models.SmallAutoField(primary_key=True)
    cert_type=models.ForeignKey(TrainingType, on_delete=models.CASCADE)
    issued_date = models.DateField(auto_now_add=True)
    certi_doc = models.FileField(upload_to='images/', default='defualt.jpg')
    awarded = models.ForeignKey(Trainer, primary_key=False, on_delete= models.CASCADE)

class Admin(Account):
    is_admin= models.BooleanField(default=False)

    def approve_agreement(self):
        return None


class Contract(models.Model):
    cont_id= models.SmallAutoField(primary_key=True)
    sign_by = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    agreement_date=models.DateField(auto_now_add=True)
    for_training = models.ForeignKey(TrainingType, on_delete=models.CASCADE)
    lasting_date = models.DateField()



    def __obj__(self):
        return self.owner







   