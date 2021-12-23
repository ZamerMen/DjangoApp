from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

def posts_list(request):
    if request.method == 'GET':
        p = Post.objects.all()
        return render(request, 'blog/index.html', context={"posts": p})

    if request.method == 'POST':
        return HttpResponse('oops i didnt it yet ')

def post_detail(request, slug):
    p = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', context={'post': p})



