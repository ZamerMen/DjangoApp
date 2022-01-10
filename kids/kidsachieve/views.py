from django.shortcuts import render, redirect
from .models import *
from django.views.generic import View, CreateView
from django.urls import reverse_lazy
from .forms import *
from .utils import *




class ChildList(View):
    def get(self, request):
        current_user = request.user
        children = Child.objects.all()
        works = Work.objects.all()
        achievements = AchieveList.objects.all()

        return render(request, 'kidsachieve/index.html',
                      context={'children': children, 'works': works, 'achievements': achievements, 'current_user': current_user}
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

class ChildAchievementsList(View):
    def get(self, request, slug):
        child = Child.objects.get(slug__iexact=slug)
        works = AchieveList.objects.filter(child_nick=child.id)
        return render(request, 'kidsachieve/child_achievements_list.html', context={'child': child, 'works': works})

class WorkDetail(View):
    def get(self, request, slug):
        work = Work.objects.get(slug__iexact=slug)
        return render(request, 'kidsachieve/work_detail.html', context={'work': work})




# class RegisterUser(DataMixin, CreateView):
#     form_class = UserCreationForm
#     template_name = 'kidsachieve/register.html'
#     success_url = reverse_lazy('login')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Register')
#         return dict(list(context.items()) + list(c_def.items()))