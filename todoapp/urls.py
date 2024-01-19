from django.urls import path
from django.contrib.auth import views as auth_views
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView,task_detail
from . import views

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('login/',views.handleLogin, name='handleLogin'),
    path('logout/', views.handleLogout, name='handleLogout'),
    path('tasks/<int:pk>/detail/', task_detail, name='task-detail'),
]
