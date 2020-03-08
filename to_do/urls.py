from django.urls import path
from . import views


app_name = "to_do"
urlpatterns = [
    path('', views.ToDoList.as_view(), name="index"),
    path("delete/<int:pk>", views.ToDoDelete.as_view(), name="delete"),
    path("create", views.ToDoCreate.as_view(), name="create"),
    path("create/<int:pk>", views.ToDoUpdate.as_view(), name="update"),
]
