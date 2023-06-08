from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Departments, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer
from django.http.response import JsonResponse
from django.core.files.storage import default_storage
@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed my Guy", safe=False)
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentID=department_data['DepartmentID'])
        departments_serializer = DepartmentSerializer(department, data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed my Guy", safe=False)
    elif request.method == 'DELETE':
        department = Departments.objects.get(DepartmentID=id)
        department.delete()
        return JsonResponse("Deleted Record", safe=False)


@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        employee = Employee.objects.all()
        employee_serializer = EmployeeSerializer(employee, many=True)
        return JsonResponse(employee_serializer.data, safe=False)
    elif request.method == 'POST':
            employee_data = JSONParser().parse(request)
            employee_serializer = EmployeeSerializer(data=employee_data)
            if employee_serializer.is_valid():
                employee_serializer.save()
                return JsonResponse("Added Successfully", safe=False)
            return JsonResponse("Failed my Guy", safe=False)
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employee.objects.get(EmployeeID=employee_data['EmployeeID'])
        employee_serializer = EmployeeSerializer(employee, data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed my Guy", safe=False)
    elif request.method == 'DELETE':
        employee = Employee.objects.get(EmployeeID=id)
        employee.delete()
        return JsonResponse("Deleted Record", safe=False)
@csrf_exempt   
def SaveFile(request):
    file = request.FILES['myfile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)
