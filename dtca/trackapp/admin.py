from django.contrib import admin
from .models import CompanyDB,Employee,Device,DeviceInfo,EmployeeUser
# Register your models here.
admin.site.register(CompanyDB)
admin.site.register(Employee)
admin.site.register(Device)
admin.site.register(DeviceInfo)
admin.site.register(EmployeeUser)
