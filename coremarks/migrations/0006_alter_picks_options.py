# Generated by Django 4.2.1 on 2023-06-04 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coremarks', '0005_remove_employee_picks_remove_picks_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='picks',
            options={'verbose_name_plural': 'Picks'},
        ),
    ]
