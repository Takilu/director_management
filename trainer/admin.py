from django.contrib import admin
from . models import Trainer, TrainingType, Certifcate, Contract, Admin, BusinessLicense
#Register your models here.
#admin.site.register(Account),
#admin.site.register(Trainer),
#admin.site.register(TrainingType)
admin.site.register(Admin)
admin.site.register(Certifcate)
#admin.site.register(Contract)

@admin.register(Contract)
class ContractApprove(admin.ModelAdmin):
    list_display=('cont_id','sign_by', 'for_training','agreement_date', 'lasting_date')
    def approve_contract(self, request, obj=None, **kwargs):
        form=super().approve_contract(request, obj, **kwargs)
        is_superuser= request.user.is_superuser

        if not is_superuser:
            form.base_fields['cont_id'].disabled=True



@admin.register(TrainingType)
class RegisterTraining(admin.ModelAdmin):
    list_display= ('training_id','t_type','description','start_date','owner')

@admin.register(Trainer)
class TrainerInfo(admin.ModelAdmin):
    list_display= ['id','email','firstName', 'lastName', 'phone_number',
                   'business_tin','ownBussiness', 'assigned_for']

@admin.register(BusinessLicense)
class BusinessInfo(admin.ModelAdmin):
    list_display =['TIN', 'given_date','expired_date']