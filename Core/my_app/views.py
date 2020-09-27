from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)

from . import models


# Create your views here.

# def index(request):
#     tasks = Task.objects.all()
#
#     form = TaskForm()
#
#     if request.method == "POST":
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('/')
#
#     context = {"tasks":tasks, "form": form}
#     return render(request, "tasks/task_list.html", context)


class TaskListView(ListView):

    model = models.Task


class TaskDetailView(DetailView):
    context_object_name = 'task_details'
    model = models.Task
    template_name = 'my_app/task_detail.html'

class TaskCreateView(CreateView):
    fields = ('title',)
    model = models.Task



class TaskUpdateView(UpdateView):
    fields = ("title", "complete")
    model = models.Task



class TaskDeleteView(DeleteView):
    model = models.Task
    success_url = reverse_lazy("my_app:list")



# def update_task(request, pk):
#     tasks = Task.objects.get(pk=pk)
#
#     form = TaskForm(instance=tasks)
#
#
#
#     if request.method == "POST":
#         form = TaskForm(request.POST, instance=tasks)
#         if form.is_valid():
#             form.save()
#         return redirect('/')
#
#     context = {"form":form}
#     return render(request, "tasks/task_update.html", context)



# def delete_task(request, pk):
#     item = Task.objects.get(pk=pk)
#
#     if request.method == "POST":
#         item.delete()
#         return redirect('/')
#
#
#     context = {"item":item}
#     return render(request, "tasks/confirm_delete.html", context)
