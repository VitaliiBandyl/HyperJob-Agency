from django import forms


class VacancyCreateForm(forms.Form):
    description = forms.CharField(max_length=1024)