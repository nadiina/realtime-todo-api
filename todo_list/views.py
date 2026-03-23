from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets, permissions
from .models import Task, AppInfo, Profile, OnlineUser
from .serializers import TaskSerializer, AppInfoSerializer, ProfileSerializer, RegisterSerializer
from .forms import TaskForm
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.contrib.auth.decorators import login_required

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        task = serializer.save()

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'tasks_group',
            {
                'type': 'task_update',
                'action': 'created',
                'task': serializer.data
            }
        )

    def perform_update(self, serializer):
        task = serializer.save()

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'tasks_group',
            {
                'type': 'task_update',
                'action': 'updated',
                'task': serializer.data
            }
        )

    def perform_destroy(self, instance):
        task_id = instance.id
        instance.delete()

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'tasks_group',
            {
                'type': 'task_update',
                'action': 'deleted',
                'task': {'id': task_id}
            }
        )


class AppInfoViewSet(viewsets.ModelViewSet):
    queryset = AppInfo.objects.all()
    serializer_class = AppInfoSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


# --- Звичайні HTML Views (залишаємо як було) ---
def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'todo_list.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})


def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'delete_confirm.html', {'task': task})

@login_required
def ws_monitor(request):
    current_online = OnlineUser.objects.all()
    return render(request, 'ws_monitor.html', {'online_users': current_online})