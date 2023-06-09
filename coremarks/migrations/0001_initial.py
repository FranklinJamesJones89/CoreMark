# Generated by Django 4.2.1 on 2023-06-03 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=500)),
                ('last_name', models.CharField(max_length=500)),
                ('employee_id', models.IntegerField()),
                ('shift', models.CharField(max_length=500)),
                ('number_of_picks', models.IntegerField()),
                ('picks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coremarks.picks')),
            ],
        ),
    ]
