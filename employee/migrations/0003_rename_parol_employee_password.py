# Generated by Django 4.1.6 on 2023-02-16 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_rename_name_employee_username_employee_parol'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='parol',
            new_name='password',
        ),
    ]