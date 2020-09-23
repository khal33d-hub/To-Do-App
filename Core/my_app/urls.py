from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="List"),
    path('edit/<str:pk>/', views.update_task, name="Edit"),
    path('delete/<str:pk>/', views.delete_task, name="delete")


]
