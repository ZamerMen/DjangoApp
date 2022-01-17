from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import View
from blog.forms import *
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .utils import *

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form = PostForm
    template = 'blog/post_create_form.html'
    raise_exeption = True


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'
    raise_exeption = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'posts_list_url'
    raise_exeption = True


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form = TagForm
    template = 'blog/tag_create.html'
    raise_exeption = True


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'
    raise_exeption = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete_form.html'
    redirect_url = 'tags_list_url'
    raise_exeption = True


def posts_list(request):
   p = Post.objects.all()
   return render(request, 'blog/index.html', context={"posts": p})


def tags_list(request):
    t = Tag.objects.all()
    return render(request, 'blog/tags.html', context={'tags': t})

