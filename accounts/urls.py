from django.contrib.admin import views
from django.urls import path
from .import views

urlpatterns = [
    path('todos/', views.create, name='create-todo'),
    path('todos/list/', views.list, name='list-todos'),
    path('todos/<int:pk>/', views.get_todo, name='get-todo'),
    path('todos/<int:pk>/update/', views.update, name='update-todo'),
    path('todos/<int:pk>/delete/', views.delete_todo, name='delete-todo'),
]