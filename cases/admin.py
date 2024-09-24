from django import forms
from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Patient, Symptom, Treatment, Case

AdminSite.site_header = "Diarrhea Surveillance Portal"
AdminSite.site_title = "Diarrhea Surveillance Portal"
AdminSite.index_title = "Welcome to Diarrhea Surveillance Portal"

class CaseAdminForm(forms.ModelForm):
    symptoms = forms.ModelMultipleChoiceField(
        queryset=Symptom.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    treatment = forms.ModelMultipleChoiceField(
        queryset=Treatment.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Patient
        fields = '__all__'


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date_of_birth', 'gender', 'contact_number')
    search_fields = ('full_name', 'gender')
    list_filter = 'gender',
    ordering = ('-id',)
    pass

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('patient', 'ward_district', 'outcome', 'onset_date', 'reported_date')
    search_fields = ('ward_district', 'outcome')
    list_filter = ('outcome', 'onset_date', 'reported_date', 'ward_district')
    ordering = ('-reported_date',)
    form = CaseAdminForm
    class Meta:
        model = Case

@admin.register(Symptom)
class SymptomAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    pass

@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    pass
