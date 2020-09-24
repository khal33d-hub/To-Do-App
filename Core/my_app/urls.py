from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="List"),
    path('edit/<int:pk>/', views.update_task, name="Edit"),
    path('delete/<int:pk>/', views.delete_task, name="delete")

]
