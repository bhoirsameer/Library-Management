from django import forms
from . models import *

class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = "__all__"

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registrations
        fields = ["name","email","password"]
