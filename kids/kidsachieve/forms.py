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
            'points': forms.NumberInput(attrs={'class': 'form-control'}),
            'comments': forms.TextInput(attrs={'class': 'form-control'})
        }

    def save(self):
        new_obj = Work.objects.create(
            title=self.cleaned_data['title'],
            points=self.cleaned_data['points'],
            comments=self.cleaned_data['comments']
        )
        return new_obj


class AchieveListForm(forms.ModelForm):

    class Meta:
        model = AchieveList
        fields = ['child_nick', 'work_title', 'comments', 'correct_point']

        widgets = {
            'child_nick': forms.Select(attrs={'class': 'form-control'}),
            'work_title': forms.Select(attrs={'class': 'form-control'}),
            'comments': forms.TextInput(attrs={'class': 'form-control'}),
            'correct_point': forms.NumberInput(attrs={'class': 'form-control'})
        }


# class AchieveListForm(forms.Form):
#     choice_child = [(x.nick_name, x.nick_name) for x in Child.objects.all()]
#     choice_work = [(x.title, x.title) for x in Work.objects.all()]
#
#     child_nick = forms.CharField(widget=forms.Select(choices=choice_child))
#     work_title = forms.CharField(widget=forms.Select(choices=choice_work))
#
#     comments = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     correct_point = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # def save(self):
    #
    #     new_obj = AchieveList.objects.create(
    #         child_nick=Child.objects.get(nick_name=self.cleaned_data['child_nick']),
    #         work_title=Work.objects.get(work_title=self.cleaned_data['work_title']),
    #         # work_title=self.cleaned_data['work_title'],
    #         comments=self.cleaned_data['comments'],
    #         correct_point=self.cleaned_data['correct_point']
    #     )
    #     return new_obj