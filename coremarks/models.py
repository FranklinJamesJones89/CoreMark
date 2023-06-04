from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    employee_id = models.IntegerField(null=True)
    items_picked = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Day(models.Model):
    date = models.DateField()
    employees = models.ManyToManyField(Employee, through='EmployeeDay')

    def __str__(self):
        return str(self.date)

class EmployeeDay(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    shift = models.CharField(max_length=500, null=True)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    items_picked = models.IntegerField()

    def __str__(self):
        return str(self.employee)


