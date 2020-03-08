from django.shortcuts import render
from .models import ToDo
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic import DeleteView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

# Create your views here.
class ToDoList(ListView):
    model = ToDo
    template_name = "to_do/index.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["all_to_dos"] = ToDo.objects.all().order_by("-date_created").order_by("-completed")
        return context


class ToDoDelete(DeleteView):
    model = ToDo
    success_url = reverse_lazy('to_do:index')

class ToDoCreate(CreateView):
    model = ToDo
    success_url = reverse_lazy('to_do:index')
    fields = ["content"]

class ToDoUpdate(UpdateView):
    model = ToDo
    success_url = reverse_lazy('to_do:index')
    fields = ["content", "completed"]
