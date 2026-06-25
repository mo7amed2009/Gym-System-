from django.urls import path
from . import views


urlpatterns=[
    
    path('create_split/', views.CreateListSplitVIew.as_view(),name='create_split'),
    path('update_split/<str:split>/', views.UpdateDeleteSplitView.as_view(),name='update_split'),
    path('insert_secondry_mucle/', views.SecondryMuscleListCreateView.as_view(), name='insert_secondry_mucle'),
    path('update_secondry_mucle/<str:name>/', views.SecondryMusclePutDelete.as_view(), name='update_secondry_mucle'),
    path('insert_exersices/', views.ExersiceListCreateView.as_view(), name='insert_exersices'),
    path('update_exerices/<str:name>/', views.ExersicePutDelete.as_view(), name='update_exerices'),
    path('create_programtemplate/', views.ProgramTempleteListCreateView.as_view(), name='create_programtemplate'),
    path('update_programtemplate/<str:name>/', views.ProgramTempletePutDelete.as_view(), name='update_programtemplate'),
    path('create_programday/', views.ProgramDayteListCreateView.as_view(), name='create_programday'),
    path('update_programday/<str:name>/', views.ProgramDayPutDelete.as_view(), name='update_programday'),
    path('create_programexersice/', views.ProgramExersiceteListCreateView.as_view(), name='create_programexersice'),
    path('update_programexersice/<slug:slug>/', views.ProgramExersicePutDelete.as_view(), name='update_programexersice'),
]