from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    ordering=['-id']


class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('task-list')
    def form_valid(self, form):
        form.instance.stage = 'todo'
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['title', 'description', 'stage']
    success_url = reverse_lazy('task-list')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('task-list')


def handleLogin(request):
    if request.method=='POST':
        loginusername=request.POST['username']
        loginpassword=request.POST['password']
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            return redirect('task-list')
        else:
            return redirect('task-list')

    return HttpResponse('handleLogin')
def handleLogout(request):
    
    logout(request)
    return redirect('task-list')
    # return HttpResponse('handleLogout')