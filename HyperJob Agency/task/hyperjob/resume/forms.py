from django import forms


class ResumeCreateForm(forms.Form):
    description = forms.CharField(max_length=1024)