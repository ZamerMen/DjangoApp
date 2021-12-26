from django import forms
from blog.models import *
from django.core.exceptions import ValidationError

class TagForm(forms.Form):
    title = forms.CharField(max_length=50)
    title.widget.attrs.update({'class': 'form-control', 'placeholder': 'title'})

    slug = forms.CharField(max_length=50)
    slug.widget.attrs.update({'class': 'form-control', 'placeholder': 'slug'})

# class TagForm(forms.Form):
#     title = forms.CharField(
#         max_length=50,
#         widget=forms.TextInput(attrs={'placeholder': 'title'})
#     )
#
#     slug = forms.CharField(
#         max_length=50,
#         widget=forms.TextInput(attrs={'placeholder': 'slug'})
#     )


    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create" ')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(f'we alredy have {new_slug} as slug')
        return new_slug



    def save(self):
        new_tag = Tag.objects.create(title=self.cleaned_data['title'], slug=self.cleaned_data['slug'])
        return new_tag