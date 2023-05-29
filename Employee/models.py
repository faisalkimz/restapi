from django.db import models


class Departments(models.Model):
    DepartmentID = models.AutoField(primary_key= True)
    DepartmentName = models.CharField(max_length=100)

class Employee(models.Model):
    EmployeeID = models.AutoField(primary_key= True)
    EmployeeName = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    dateofjoining = models.DateField()
    Photofilename = models.CharField(max_length= 100)
