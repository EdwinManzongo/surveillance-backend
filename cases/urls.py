from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'patients', views.PatientViewSet)
router.register(r'cases',  views.CaseViewSet)
router.register(r'symptoms', views.SymptomViewSet)
router.register(r'treatments', views.TreatmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]