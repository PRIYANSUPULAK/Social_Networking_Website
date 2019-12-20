from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.ListGroups.as_view(), name="all"),
    path("new/", views.CreateGroup.as_view(), name="create"),
    #Here Slug parameter is used in place of primary key but one should use both slug as well as pk.
    #Slug is a attribute of Posts.
    path("posts/in/<slug>/",views.SingleGroup.as_view(),name="single"),
    path("join/<slug>/",views.JoinGroup.as_view(),name="join"),
    path("leave/<slug>/",views.LeaveGroup.as_view(),name="leave"),
]
