from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index,),
    path('delete-recipe/<id>/',views.delete,name="delete")
]
