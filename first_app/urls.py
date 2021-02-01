from django.urls import path
from . import views

urlpatterns = [
    path("", views.index , name="index"),
    path("mallika",views.mallika, name="mallika"),
    path("shlagha", views.shlagha, name="shlagha"),
    path("<str:name>", views.greet, name="greet"),
    path("<str:name>/greet_hello", views.greet_hello, name="greet_hello")
]



