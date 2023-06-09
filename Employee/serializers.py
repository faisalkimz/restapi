from rest_framework import serializers
from .models import Departments, Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentID', 'DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('EmployeeID', 'EmployeeName', 'DepartmentName', 'dateofjoining', 'Photofilename')