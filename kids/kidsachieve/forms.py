from django import forms

class ChildForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    nick_name = forms.CharField(max_length=50)
    age = forms.IntegerField()