from django import forms
from django.core import validators
from studentrecords.models import Students

class StudentForm(forms.ModelForm):

    class Meta:
        model = Students
        fields = "__all__"
