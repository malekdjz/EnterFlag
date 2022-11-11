from django.urls import path
from main.views import *
urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('login/',Login.as_view(),name='login'),
    path('register/',Register.as_view(),name='register'),
    path('profile/<str:username>',Profile.as_view(),name='profile'),
    path('team/<str:name>',TeamDetail.as_view(),name='team-detail'),
    path('teams/',TeamList.as_view(),name='team-list'),
    path('challanges/',ChallangeList.as_view(),name='challange-list'),
    path('challange/<str:name>',ChallangeDetail.as_view(),name='challange-detail'),
    path('about/',About.as_view(),name='about'),
    path('dashboard/',Dashboard.as_view(),name='dashboard'),

]