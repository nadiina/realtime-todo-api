from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from todo_list.views import add_task, edit_task, delete_task, ws_monitor
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('admin/', admin.site.urls),

    path('api/', include('todo_list.urls')),

    path('', add_task, name='add_task'),
    path('edit/<int:pk>/', edit_task, name='edit_task'),
    path('delete/<int:pk>/', delete_task, name='delete_task'),
    path('monitor/', ws_monitor, name='ws_monitor'),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]