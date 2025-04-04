from django.urls import path,include
from .views import ScanUploadView

from rest_framework.routers import DefaultRouter
from .views import PatientViewSet,PatientListView
from .views import RegisterUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  # Generates access & refresh tokens
    TokenRefreshView,  # Refresh access token
)
router = DefaultRouter()
router.register(r'patients', PatientViewSet,basename="patients")


urlpatterns = [
    path('patients/', PatientListView.as_view(), name='patient-list'),
    path('', include(router.urls)),
    path('upload-scan/', ScanUploadView.as_view(), name='upload-scan'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterUserView.as_view(), name='register'),
]

