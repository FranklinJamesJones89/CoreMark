# Generated by Django 4.2.1 on 2023-06-04 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coremarks', '0008_day_shift_employee_employee_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='shift',
        ),
        migrations.AddField(
            model_name='employeeday',
            name='shift',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
