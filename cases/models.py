from django.db import models


GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female')
]

DISTRICT = [
    ('Ward 1', 'Ward 1'),
    ('Ward 2', 'Ward 2'),
    ('Ward 3', 'Ward 3'),
    ('Ward 4', 'Ward 4'),
    ('Ward 5', 'Ward 5'),
    ('Ward 6', 'Ward 6'),
    ('Ward 7', 'Ward 7'),
    ('Ward 8', 'Ward 8'),
    ('Ward 9', 'Ward 9'),
    ('Ward 10', 'Ward 10')
]

OUTCOME = [
    ('Resolved', 'Resolved'),
    ('Ongoing', 'Ongoing'),
    ('Fatal', 'Fatal')
]

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20, choices=GENDER)
    address = models.TextField()
    contact_number = models.CharField(max_length=20)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    full_name.short_description = 'Full Name'

    def __str__(self):
        return self.full_name()

class Case(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    onset_date = models.DateField()
    reported_date = models.DateField(auto_now_add=True)
    ward_district = models.CharField(max_length=20, choices=DISTRICT)
    symptoms = models.ManyToManyField('Symptom', blank=True)
    treatment = models.ManyToManyField('Treatment', blank=True)
    outcome = models.CharField(max_length=20, choices=OUTCOME)

    def __str__(self):
        id_str = str(self.id)
        patient_str = self.patient or "Jane Doe"

        return f"Case {id_str}: {patient_str}"

class Symptom(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Treatment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name