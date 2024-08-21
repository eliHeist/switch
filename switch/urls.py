from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include("main.urls", namespace="main")),
    path('auth_check/', include("auth_check.urls", namespace="auth_check")),
    path('tasks/', include("tasks.urls", namespace="tasks")),
    path('users/', include("users.urls", namespace="users")),
]
