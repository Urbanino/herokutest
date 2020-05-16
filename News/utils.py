from django.shortcuts import render, redirect, reverse
from .forms import NoteForm, TagForm
from .models import Tags, Notes, Comments

class ObjCreateMixin: 
    model_form = None
    template = None
    

    def get(self, request, *args, **kwargs):
        form = self.model_form()
        return render(request, self.template, context={'form': form})

    def post(self, request, *args, **kwargs):
        bound_form = self.model_form(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})

class ObjUpdateMixin:
    data = None
    model_form = None
    template = None

    def get(self, request, obj_id):
        data_obj = self.data.objects.get(pk=obj_id)
        bound_form = self.model_form(instance=data_obj)
        return render(request, self.template, context={'form': bound_form, 'obj': data_obj})

    def post(self, request, obj_id):
        data_obj = self.data.objects.get(pk=obj_id)
        bound_form = self.model_form(request.POST, instance=data_obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form, 'obj': data_obj})

class ObjDeleteMixin:
    data = None
    template = None

    def get(self, request, obj_id):
        data_obj = self.data.objects.get(pk=obj_id)
        return render(request, self.template, context={'obj': data_obj})

    def post(self, request, obj_id):
        data_obj = self.data.objects.get(pk=obj_id)
        data_obj.delete()
        return redirect(reverse('url_index'))








