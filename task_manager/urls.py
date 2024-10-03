# task_manager/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path('tasks/', include('tasks.urls')),  
]

