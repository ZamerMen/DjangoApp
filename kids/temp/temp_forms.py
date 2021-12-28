from django import forms
from .models import *

class ChildForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    nick_name = forms.CharField(max_length=50)
    age = forms.IntegerField()

    def save(self):
        new_child = Child.objects.create(
            first_name=self.cleaned_data['first_name'],
            nick_name=self.cleaned_data['nick_name'],
            age=self.cleaned_data['age']
        )
        return new_child