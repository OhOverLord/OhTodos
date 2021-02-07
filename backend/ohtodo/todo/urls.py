from django.urls import path
from .views import TodoListAPI, delete_todo, todo_status


urlpatterns = [
    path('todo-list/', TodoListAPI.as_view(), name='todo-list'),
    path('delete-todo/<int:pk>', delete_todo, name='delete-todo'),
    path('todo-status/<int:pk>', todo_status, name='todo_status'),
]