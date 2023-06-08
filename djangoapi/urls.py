from django.contrib import admin
from django.urls import path, include 
from Employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Employee.urls')),
]


