# Generated by Django 5.1.1 on 2024-09-18 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0002_remove_patient_gender_patient_outcome'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='outcome',
            new_name='gender',
        ),
    ]
