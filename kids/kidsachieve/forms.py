from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    field_order = ['username', 'email', 'password1', 'password2']


class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['first_name', 'nick_name', 'age']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'nick_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'})
        }


    # def save(self):
    #     new_obj = Child.objects.create(
    #         first_name=self.cleaned_data['first_name'],
    #         nick_name=self.cleaned_data['nick_name'],
    #         age=self.cleaned_data['age']
    #     )
    #     return new_obj


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['title', 'point', 'comment']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'point': forms.NumberInput(attrs={'class': 'form-control'}),
            'comment': forms.TextInput(attrs={'class': 'form-control'})
        }

    # def save(self):
    #     new_obj = Work.objects.create(
    #         title=self.cleaned_data['title'],
    #         points=self.cleaned_data['point'],
    #         comments=self.cleaned_data['comment']
    #     )
    #     return new_obj


class AchieveListForm(forms.ModelForm):

    class Meta:
        model = AchieveList
        fields = ['child_nick', 'work_title', 'comment', 'benefit_point']

        widgets = {
            'child_nick': forms.Select(attrs={'class': 'form-control'}),
            'work_title': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.TextInput(attrs={'class': 'form-control'}),
            'benefit_point': forms.NumberInput(attrs={'class': 'form-control'})
        }
