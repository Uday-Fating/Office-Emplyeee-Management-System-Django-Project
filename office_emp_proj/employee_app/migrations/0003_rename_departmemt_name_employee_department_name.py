# Generated by Django 5.0.6 on 2024-07-07 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0002_rename_departmemtname_employee_departmemt_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='departmemt_name',
            new_name='department_name',
        ),
    ]
