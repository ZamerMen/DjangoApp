from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     field_order = ['username', 'email', 'password1', 'password2']


class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['first_name', 'nick_name', 'age']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'nick_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'})
        }


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['title', 'point', 'comment']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'point': forms.NumberInput(attrs={'class': 'form-control'}),
            'comment': forms.TextInput(attrs={'class': 'form-control'})
        }


class AchievementForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['child_nick'].queryset = Child.objects.filter(user=user)
        self.fields['work_title'].queryset = Work.objects.filter(user=user)

    class Meta:
        model = Achievement
        fields = ['child_nick', 'work_title', 'comment', 'benefit_point']

        widgets = {
            'child_nick': forms.Select(attrs={'class': 'form-control'}),
            'work_title': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.TextInput(attrs={'class': 'form-control'}),
            'benefit_point': forms.NumberInput(attrs={'class': 'form-control'})
        }
