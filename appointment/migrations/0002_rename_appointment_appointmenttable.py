# Generated by Django 5.0.1 on 2024-03-20 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Appointment',
            new_name='AppointmentTable',
        ),
    ]
