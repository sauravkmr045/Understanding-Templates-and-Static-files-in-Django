
from django.urls import path
from app1 import views

urlpatterns = [

    path('models', views.model),
    path('myform', views.myform),

]
