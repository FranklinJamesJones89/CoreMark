from django.contrib import admin

# Register your models here.

from .models import Day, EmployeeDay, Employee

admin.site.register(Day)
admin.site.register(EmployeeDay)
admin.site.register(Employee)
