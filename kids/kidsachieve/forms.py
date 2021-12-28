from django import forms
from .models import *

class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['first_name', 'nick_name', 'age']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'nick_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'})
        }


    def save(self):
        new_obj = Child.objects.create(
            first_name=self.cleaned_data['first_name'],
            nick_name=self.cleaned_data['nick_name'],
            age=self.cleaned_data['age']
        )
        return new_obj


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['title', 'points', 'comments']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'points': forms.TextInput(attrs={'class': 'form-control'}),
            'comments': forms.TextInput(attrs={'class': 'form-control'})
        }

    def save(self):
        new_obj = Work.objects.create(
            title=self.cleaned_data['title'],
            points=self.cleaned_data['points'],
            comments=self.cleaned_data['comments']
        )
        return new_obj


class AchieveListForm(forms.Form):
    choice_child = [(x.id, x.nick_name) for x in Child.objects.all()]
    choice_work = [(x.id, x.title) for x in Work.objects.all()]

    child_id = forms.CharField(widget=forms.Select(choices=choice_child))
    work_id = forms.CharField(widget=forms.Select(choices=choice_work))



    def save(self):
        print(self.cleaned_data)

        Child.
        new_obj = AchieveList.objects.create(
           child_id=child_id.set(self.cleaned_data['child_id'],)
           work_id=self.cleaned_data['work_id']
        )
        return new_obj