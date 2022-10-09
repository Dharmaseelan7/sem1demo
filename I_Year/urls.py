from django.urls import path
from . import views

# Admin Views
urlpatterns = [
    path('apiOverView/', views.ApiOverView.as_view()),
    path('results/IT/', views.Sem_1_Results_List_View_IT.as_view()),
    path('results/IT/<int:pk>/', views.Sem_1_Result_IT_View.as_view()),
    path('results/CSE/', views.Sem_1_Results_List_View_CSE.as_view()),
    path('results/CSE/<int:pk>/', views.Sem_1_Result_CSE_View.as_view()),
    path('results/ECE/', views.Sem_1_Results_List_View_ECE.as_view()),
    path('results/ECE/<int:pk>/', views.Sem_1_Result_ECE_View.as_view()),
    path('results/EEE/', views.Sem_1_Results_List_View_EEE.as_view()),
    path('results/EEE/<int:pk>/', views.Sem_1_Result_EEE_View.as_view()),
    path('results/AIDS/', views.Sem_1_Results_List_View_AIDS.as_view()),
    path('results/AIDS/<int:pk>/', views.Sem_1_Result_AIDS_View.as_view()),
    path('results/MECH/', views.Sem_1_Results_List_View_MECH.as_view()),
    path('results/MECH/<int:pk>/', views.Sem_1_Result_MECH_View.as_view()),
    path('results/CIVIL/', views.Sem_1_Results_List_View_CIVIL.as_view()),
    path('results/CIVIL/<int:pk>/', views.Sem_1_Result_CIVIL_View.as_view()),
    path('results/EIE/', views.Sem_1_Results_List_View_EIE.as_view()),
    path('results/EIE/<int:pk>/', views.Sem_1_Result_EIE_View.as_view()),
    path('results/AUTO/', views.Sem_1_Results_List_View_AUTO.as_view()),
    path('results/AUTO/<int:pk>/', views.Sem_1_Result_AUTO_View.as_view())
]
