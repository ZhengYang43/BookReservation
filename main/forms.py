from django import forms
from .models import Student, Book

class ReservationForm(forms.Form):
    student = forms.ModelChoiceField(queryset=Student.objects.all())
    book = forms.ModelChoiceField(queryset=Book.objects.filter(currently_checked_out=False))
