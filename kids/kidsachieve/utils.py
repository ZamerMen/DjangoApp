from django.shortcuts import render, redirect


class ObjectCreateMixin():
    form = None
    head_title = None
    ref_url = None

    def get(self, request):
        form = self.form
        return render(request, self.ref_url, context={'form': form, 'head_title': self.head_title})

    def post(self, request):
        bound_form = self.form(request.POST)
        current_user = request.user
        if bound_form.is_valid():
            new_obj = bound_form.save(commit=False)
            new_obj.user = current_user
            new_obj.save()
            return redirect('index_kidsachieve_url')
        return render(request, self.ref_url, context={'form': bound_form, 'head_title': self.head_title})


class ObjectUpdateMixin:
    form = None
    template = None
    model = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        form = self.form(instance=obj)
        return render(request, self.template, context={'form': form})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form(request.POST, instance=obj)
        if bound_form.is_valid():
            obj.save()
            return redirect(obj)
        return render(request, self.template, context={'form': bound_form})


class ObjectDeleteMixin:
    model = None
    template = None
    url_redirect = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={'obj': obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(self.url_redirect)