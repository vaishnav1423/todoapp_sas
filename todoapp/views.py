from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from django.utils import timezone
from django.shortcuts import render, get_object_or_404


import logging

logger = logging.getLogger(__name__)

class TaskListView(ListView):
    logging.info(f"Tasklist View Home Page")
    model = Task
    template_name = 'task_list.html'
    ordering=['-id']
    def get_queryset(self):
        if self.request.user.is_authenticated:
            logging.info(f"User ${self.request.user} is Authenticated  ")
            return Task.objects.filter(user=self.request.user)
        else:
            logging.info(f"User is not authenticated  ")
            return Task.objects.none()


class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('task-list')
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            form.instance.stage = 'todo'
            return super().form_valid(form)
        else:
            # Handle the case where the user is not authenticated
            return self.handle_no_permission()

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['title', 'description', 'stage']
    success_url = reverse_lazy('task-list')
    def form_valid(self, form):
        task = form.save(commit=False)
        if task.stage == 'done' and not task.completed_at:
            task.completed_at = timezone.now()
        task.save()
        return super().form_valid(form)
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Task.objects.filter(user=self.request.user)
        else:
            return Task.objects.none()

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('task-list')
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Task.objects.filter(user=self.request.user)
        else:
            return Task.objects.none()


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

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task': task})