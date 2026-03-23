from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet, basename='task')
router.register(r'appinfo', views.AppInfoViewSet, basename='appinfo')
router.register(r'profile', views.ProfileViewSet, basename='profile')
router.register(r'register', views.RegisterViewSet, basename='register')

urlpatterns = [
    path('', include(router.urls)),

    # path('list/', views.task_list, name='task_list'),
    # path('create/', views.add_task, name='add_task'),
]