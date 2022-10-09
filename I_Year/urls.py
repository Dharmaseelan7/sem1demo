from django.urls import path
from .views import views1

# Admin Views
# -------------------SEM-1----------------------
urlpatterns = [
    path('apiOverView/', views1.ApiOverView.as_view()),
    path('results/IT/', views1.Sem_1_Results_List_View_IT.as_view()),
    path('results/IT/<int:pk>/', views1.Sem_1_Result_IT_View.as_view()),
    path('results/CSE/', views1.Sem_1_Results_List_View_CSE.as_view()),
    path('results/CSE/<int:pk>/', views1.Sem_1_Result_CSE_View.as_view()),
    path('results/ECE/', views1.Sem_1_Results_List_View_ECE.as_view()),
    path('results/ECE/<int:pk>/', views1.Sem_1_Result_ECE_View.as_view()),
    path('results/EEE/', views1.Sem_1_Results_List_View_EEE.as_view()),
    path('results/EEE/<int:pk>/', views1.Sem_1_Result_EEE_View.as_view()),
    path('results/AIDS/', views1.Sem_1_Results_List_View_AIDS.as_view()),
    path('results/AIDS/<int:pk>/', views1.Sem_1_Result_AIDS_View.as_view()),
    path('results/MECH/', views1.Sem_1_Results_List_View_MECH.as_view()),
    path('results/MECH/<int:pk>/', views1.Sem_1_Result_MECH_View.as_view()),
    path('results/CIVIL/', views1.Sem_1_Results_List_View_CIVIL.as_view()),
    path('results/CIVIL/<int:pk>/', views1.Sem_1_Result_CIVIL_View.as_view()),
    path('results/EIE/', views1.Sem_1_Results_List_View_EIE.as_view()),
    path('results/EIE/<int:pk>/', views1.Sem_1_Result_EIE_View.as_view()),
    path('results/AUTO/', views1.Sem_1_Results_List_View_AUTO.as_view()),
    path('results/AUTO/<int:pk>/', views1.Sem_1_Result_AUTO_View.as_view())
]
# -----------------END OF SEM-1-------------------------------
