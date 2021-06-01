from django.urls import path
from . import views

# create your own path

urlpatterns = [
    # step 7 :
    path('', views.index,name = "list"),
    # step 17 :
    path('update_tasks/<str:pk>',views.updateTask,name="update_tasks"),
    # step 18 :
    path('delete/<str:pk>',views.deleteTask,name="Delete")
]