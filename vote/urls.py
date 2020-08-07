from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("", views.all, name="home"),
    path("vote/<str:name>", views.vote, name="vote"),
    path("home/<str:name>", views.hack, name="land"),
    path("admin1", views.admin, name="admin"),
    path("candidate", views.candidate, name="candidate"),
    path("user", views.user, name="user"),
    path("rest/hacker", views.hackers.as_view(),name="hacker_add"),
    path("rest/hacker/<str:hacker>/<str:password>", views.hackers.as_view(),name="hacker"),
]