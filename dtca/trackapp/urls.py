from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, EmployeeUserViewSet, EmployeeViewSet, DeviceViewSet, DeviceInfoViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeUserViewSet)
router.register(r'employeedetails', EmployeeViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'deviceinfo', DeviceInfoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]