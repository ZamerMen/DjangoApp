from django.shortcuts import render, redirect
from .models import *
from django.views.generic import View
from .forms import *
from .utils import *


class ChildList(View):
    def get(self, request):
        children = Child.objects.all()
        works = Work.objects.all()
        achievements = AchieveList.objects.all()

        return render(request, 'kidsachieve/index.html',
                      context={'children': children, 'works': works, 'achievements': achievements}
                      )


class ChildCreate(ObjectCreateMixin, View):
    form = ChildForm
    head_title = "Create child account"
    ref_url = 'kidsachieve/child_create.html'


class WorkCreate(ObjectCreateMixin, View):
    form = WorkForm
    head_title = "Create works"
    ref_url = 'kidsachieve/work_create.html'


class AchievementCreate(View):
    head_title = "Create achievements in works"

    def get(self, request):
        form = AchieveListForm()
        return render(request, 'kidsachieve/achievement_create.html', context={'form': form})

    def post(self, request):
        bound_form = AchieveListForm(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect('index_kidsachieve_url')
        return render(request, 'kidsachieve/achievement_create', context={'form': bound_form})