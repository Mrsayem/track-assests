from rest_framework import viewsets
from .models import CompanyDB, EmployeeUser, Employee, Device, DeviceInfo
from .serializers import CompanySerializer, EmployeeUserSerializer, EmployeeSerializer, DeviceSerializer, DeviceInfoSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = CompanyDB.objects.all()
    serializer_class = CompanySerializer

class EmployeeUserViewSet(viewsets.ModelViewSet):
    queryset = EmployeeUser.objects.all()
    serializer_class = EmployeeUserSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceInfoViewSet(viewsets.ModelViewSet):
    queryset = DeviceInfo.objects.all()
    serializer_class = DeviceInfoSerializer
