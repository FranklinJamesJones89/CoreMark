# Generated by Django 4.2.1 on 2023-06-03 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coremarks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picks',
            name='date',
            field=models.TextField(),
        ),
    ]