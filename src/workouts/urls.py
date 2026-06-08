from django.urls import path
from .views import SplitListView, CreateProgramExersiceView, UpdateProgramExersiceView,ExersicesListView,EquipmentListView


urlpatterns=[
    path('split_systems/',SplitListView.as_view()),
    path('create_exersice/',CreateProgramExersiceView.as_view()),
    path('update_program/<slug:slug>/',UpdateProgramExersiceView.as_view()),
    path('all_exersices/',ExersicesListView.as_view()),
    path('equipments/',EquipmentListView.as_view())
    
#     path('split_systems/<str:system>/',SplitDetilsView.as_view())
]