from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="task_home"),
    path('add/', views.add_task, name="task_add"),
    path("complete/<int:pk>/",views.mark_complete, name="task_complete"),
    path("delete/<int:pk>/",views.delete_task, name="task_delete"),
]
