# Generated by Django 4.2.1 on 2023-05-28 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('EmployeeID', models.AutoField(primary_key=True, serialize=False)),
                ('EmployeeName', models.CharField(max_length=100)),
                ('Department', models.CharField(max_length=100)),
                ('dateofjoining', models.DateField()),
                ('Photofilename', models.CharField(max_length=100)),
            ],
        ),
    ]
