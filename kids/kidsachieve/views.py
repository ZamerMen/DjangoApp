from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views.generic import View, CreateView
from django.urls import reverse_lazy
from .forms import *
from .utils import *
from django.db.models import Sum


class ChildList(View):
    def get(self, request):
        current_user = request.user.id
        children = Child.objects.filter(user_id=current_user)
        works = Work.objects.filter(user_id=current_user)
        achievements = Achievement.objects.filter(user_id=current_user).order_by('date_done')[0:5]


        return render(request, 'kidsachieve/index.html',
                      context={'children': children,
                               'works': works,
                               'ach_lst': achievements, 'current_user': current_user
                               }
                      )


class ChildAchievementsList(View):
    def get(self, request, slug):
        child = Child.objects.get(slug__iexact=slug)
        ach_lst = Achievement.objects.filter(child_nick=child.id).order_by('date_done')
        sum_ben_points = ach_lst.aggregate(Sum('benefit_point')).get('benefit_point__sum')
        sum_work_points = 0
        for ach in ach_lst:
            sum_work_points += ach.work_title.point
        total_sum = sum_work_points + sum_ben_points
        return render(request, 'kidsachieve/child_achievements_list.html',
                      context={'child': child,
                               'ach_lst': ach_lst,
                               'sum_work_points': sum_work_points,
                               'sum_ben_points': sum_ben_points,
                               'total_sum': total_sum})


### Child ###
class ChildDetail(View):
    def get(self, request, slug):
        obj = get_object_or_404(Child, slug__iexact=slug)
        return render(request, 'kidsachieve/child_detail.html', context={'child': obj})


class ChildCreate(ObjectCreateMixin, View):
    form = ChildForm
    head_title = "Create child account"
    ref_url = 'kidsachieve/child_create.html'


class ChildUpdate(ObjectUpdateMixin, View):
    form = ChildForm
    template = 'kidsachieve/child_update.html'
    model = Child

class ChildDelete(ObjectDeleteMixin, View):
    model = Child
    template = 'kidsachieve/child_delete.html'
    url_redirect = 'index_kidsachieve_url'


### Work ###
class WorkDetail(View):
    def get(self, request, slug):
        work = Work.objects.get(slug__iexact=slug)
        return render(request, 'kidsachieve/work_detail.html', context={'work': work})


class WorkCreate(ObjectCreateMixin, View):
    form = WorkForm
    head_title = "Create works"
    ref_url = 'kidsachieve/work_create.html'


class WorkUpdate(ObjectUpdateMixin, View):
    form = WorkForm
    template = 'kidsachieve/work_update.html'
    model = Work


class WorkDelete(ObjectDeleteMixin, View):
    model = Work
    template = 'kidsachieve/work_delete.html'
    url_redirect = 'index_kidsachieve_url'


class WorksList(View):
    def get(self, request):
        current_user = request.user
        works = Work.objects.filter(user=current_user)
        return render(request, 'kidsachieve/works_list.html',
                      context={'works': works, 'current_user': current_user})


### Achievements ###
class AchievementCreate(View):
    # head_title = "Create achievements in works"

    def get(self, request):
        current_user = request.user
        form = AchievementForm(user=current_user)
        return render(request, 'kidsachieve/achievement_create.html', context={'form': form})

    def post(self, request):
        current_user = request.user
        bound_form = AchievementForm(current_user, request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save(commit=False)
            new_obj.user = current_user
            new_obj.save()
            return redirect('index_kidsachieve_url')
        return render(request, 'kidsachieve/achievement_create', context={'form': bound_form})



class AchievementUpdate(View):

    def get(self, request, slug):
        current_user = request.user
        obj = Achievement.objects.get(slug__iexact=slug)
        form = AchievementForm(current_user, instance=obj)
        return render(request, 'kidsachieve/Achievement_update.html', context={'form': form})

    def post(self, request, slug):
        current_user = request.user
        obj = Achievement.objects.get(slug__iexact=slug)
        bound_form = AchievementForm(current_user, request.POST, instance=obj)
        if bound_form.is_valid():
            obj.save()
            slug = obj.child_nick.slug
            return redirect('child_achievements_list_url', slug=slug)
        return render(request, 'kidsachieve/Achievement_update.html', context={'form': bound_form})


class AchievementDelete(ObjectDeleteMixin, View):
    model = Achievement
    template = 'kidsachieve/Achievement_delete.html'
    url_redirect = 'index_kidsachieve_url'

