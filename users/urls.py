from django.urls import path
from . import views
from .views import SignUpView


urlpatterns = [
    path('', views.landing_page, name = 'landing_page'),
    path('add/', views.add_users, name='add_users'),
    path('list_all/', views.list_all_users, name='list_all_users'),
    path('home/', views.home_page, name='home_page'),
    path('user/<id>/',views.detail_view, name="user_details"),
    path('update_user/<int:id>/', views.update_user, name='update_user'),
    path('delete_user/<int:id>/', views.delete_user, name='delete_user'),
    path("signup/", SignUpView.as_view(), name="signup"),
    #path('login/', views.login, name='login' ),
    path('dashboard/', views.admin_dashboard, name='dashboard'),
    path('profile/', views.user_profile, name='profile'),
    path('user_dashboard', views.user_dashboard, name='user_dashboard')
]