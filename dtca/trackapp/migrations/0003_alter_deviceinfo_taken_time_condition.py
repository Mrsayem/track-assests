# Generated by Django 4.2.11 on 2024-03-28 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackapp', '0002_employeeuser_alter_employee_employeename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceinfo',
            name='taken_time_condition',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
