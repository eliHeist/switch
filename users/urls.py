from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    # path('list/', views.UserListView.as_view(), name='list'),
    path('create/', views.UserCreateAPIView.as_view(), name='create'),
    # path('update/<int:pk>/', views.UserCUView.as_view(), name='update'),
]