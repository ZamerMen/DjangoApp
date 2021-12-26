from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import View
from blog.forms import TagForm


from .models import *
from .utils import ObjectDetailMixin

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'



class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_create.html', context={'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'blog/tag_create.html', context={'form': bound_form})



def posts_list(request):
   p = Post.objects.all()
   return render(request, 'blog/index.html', context={"posts": p})


def tags_list(request):
    t = Tag.objects.all()
    return render(request, 'blog/tags.html', context={'tags': t})

