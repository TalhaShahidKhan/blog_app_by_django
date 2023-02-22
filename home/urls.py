from django.urls import path
from home.views import signuppage,homepage,profilepage
urlpatterns = [
    path('auth/signup/',signuppage,name='signup'),
    path('',homepage,name='home'),
    path('profile/',profilepage,name='profile'),
]

app_name='home'