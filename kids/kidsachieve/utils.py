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
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect('index_kidsachieve_url')
        return render(request, self.ref_url, context={'form': bound_form, 'head_title': self.head_title})