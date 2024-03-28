from django.db import models

# My  models is here.
class CompanyDB(models.Model): #this is for company name like : google ,facebook , Repliq
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
class EmployeeUser(models.Model): # employee information 
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.username
class Employee(models.Model): #this is to connect the employee info and company info
    EmployeeName =  models.OneToOneField(EmployeeUser,on_delete= models.CASCADE)
    company = models.ForeignKey(CompanyDB, on_delete=models.CASCADE)
    def __str__(self):
        return self.EmployeeName.username
class Device(models.Model): #device name and condition will be stored here 
    name = models.CharField(max_length=30)
    device_condition = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class DeviceInfo(models.Model): #this will take the device field , employee field and others info 
    device = models.ForeignKey(Device, on_delete= models.CASCADE, verbose_name="Device Name")
    employee = models.ForeignKey(Employee,on_delete = models.CASCADE, verbose_name="Employee Name")
    device_given = models.DateField(null=True, blank=True, verbose_name="Given Date")
    device_taken = models.DateField( verbose_name="Device Taken Date")
    given_time_condition = models.CharField(max_length = 30,null=True, blank=True, verbose_name="Given Time Condition")
    taken_time_condition = models.CharField(max_length = 30,null=True, blank=True,  verbose_name="Taken Time Condition")
    def __str__(self):
        return self.device.name + " Given  to "+ self.employee.EmployeeName.username