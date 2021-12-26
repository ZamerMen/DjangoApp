from django.shortcuts import render
from .models import *
from django.views.generic import View
from .forms import *


class ChildList(View):
    def get(self, request):
        children = Child.objects.all()
        works = Work.objects.all()
        achievements = AchieveList.objects.all()

        return render(request, 'kidsachieve/index.html',
                      context={'children': children, 'works': works, 'achievements': achievements}
                      )


class ChildCreate(View):
    def get(self, request):
        form = ChildForm()
        return render(request, 'kidsachieve/child_create.html', context={'form': form})



def work_create(request):
    pass


def achievement_create():
    pass