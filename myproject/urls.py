from django.contrib import path
from . import views 

urlpatterns = [
    path("", views.index),
    path('about', views.about), 
    path("hello/<str:username>",views.hello),
    path("operation/<int:number>", views.operation),
    path("projects", views.projects),
    path("Taks/<int:id>, views.tasks"), 
]
