from django.urls import path
from home.views import signuppage 
urlpatterns = [
    path('auth/signup/',signuppage,name='signup')
]

app_name='home'