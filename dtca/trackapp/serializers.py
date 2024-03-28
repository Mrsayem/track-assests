from rest_framework import serializers
from .models import CompanyDB, EmployeeUser, Employee, Device, DeviceInfo

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyDB
        fields = '__all__'

class EmployeeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeUser
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class DeviceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceInfo
        fields = '__all__'
