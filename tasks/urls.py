from django.urls import path
from .views import page, user_login, user_logout, task_view, post_detail, post_new, post_edit, RegisterUser

urlpatterns = [
    path ('main/', page, name='main_page'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('task/', task_view, name='tasks'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/new/', post_new, name='post_new'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('register/', RegisterUser.as_view(), name='register'),
]

