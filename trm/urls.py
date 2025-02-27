
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from trainer import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


router = DefaultRouter()

router.register(r'trainers', views.TrainerAccountViewSet)
router.register(r'admins', views.AdminAccountViewSet)
router.register(r'training-types', views.TrainingTypeViewSet)
router.register(r'contracts', views.ContractViewSet)
router.register(r'certificate',views.CertificateViewSet)
router.register(r'business-info', views.BusinessViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('', include(router.urls))
]


