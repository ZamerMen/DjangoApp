from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterUser(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


# class RegisterUser(View):
#     def get(self, request):
#         form = UserRegisterForm()
#         return render(request, 'register.html', context={'form': form})
#
#     def post(self, request):
#         bound_form = UserRegisterForm(request.POST)
#         if bound_form.is_valid():
#             new_used = bound_form.save()
#             return print('ok')#redirect('login')
#         return render(request, 'register.html', context={'form': bound_form})
