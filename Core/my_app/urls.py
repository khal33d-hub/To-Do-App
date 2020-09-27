from django.urls import path
from .import views

app_name = 'my_app'

urlpatterns = [
    path('',views.TaskListView.as_view(),name='list'),
    path('<int:pk>/',views.TaskDetailView.as_view(),name='detail'),
    path('create/',views.TaskCreateView.as_view(),name='create'),
    path('update/<int:pk>/',views.TaskUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name="delete")

]
