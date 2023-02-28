from django.urls import path
from home.views import signuppage,homepage,profilepage,profileupdate,dltprof
urlpatterns = [
    path('auth/signup/',signuppage,name='signup'),
    path('',homepage,name='home'),
    path('profile/',profilepage,name='profile'),
    path('profile/<str:username>/upd/',profileupdate,name='profile_upd'),
    path('profile/<str:username>/dlt/',dltprof,name='profile_dlt'),
]

app_name='home'