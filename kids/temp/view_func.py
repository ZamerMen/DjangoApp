def posts_list(request):
    if request.method == 'GET':
        p = Post.objects.all()
        return render(request, 'blog/index.html', context={"posts": p})

    if request.method == 'POST':
        return HttpResponse('oops i didnt it yet ')


class TagDetail(View):
    def get(self, request, slug):
        t = Tag.objects.get(slug__iexact=slug)
        return render(request, 'blog/tag_detail.html', context={'tag': t})



class TagForm(forms.Form):
    title = forms.CharField(max_length=50)
    title.widget.attrs.update({'class': 'form-control', 'placeholder': 'title'})

    slug = forms.CharField(max_length=50)
    slug.widget.attrs.update({'class': 'form-control', 'placeholder': 'slug'})