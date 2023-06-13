from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout_user, name='logout'),
    path('update_profile/', views.update_user_profile, name='update_profile'),
    path('profile/', views.user_profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.password_change, name='change_password'),
    
]
