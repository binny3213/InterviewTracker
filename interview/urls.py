from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'interview'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('interview/interview_list', views.interview_list, name='interview_list'),
    path('create/', views.create_interview, name='create_interview'),
    path('interview/<int:pk>/update/', views.update_interview, name='update_interview'),
    path('interview/<int:pk>/delete/', views.InterviewDeleteView.as_view(), name='delete_interview'),
    path('interview/<int:pk>/', views.interview_detail, name='interview_detail'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
