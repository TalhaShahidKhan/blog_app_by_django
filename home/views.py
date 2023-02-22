from django.shortcuts import render,redirect
from home.forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def landingpage(request):
  return render(request, 'home/landingpage.html')

@login_required(login_url='login')
def homepage(request):
  return render(request, 'home/home.html')


@login_required(login_url='login')
def profilepage(request):
  return render(request, 'home/profile.html')



def signuppage(request):
  form=CustomUserCreationForm()
  if request.method == "POST":
    form=CustomUserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
  else:
    form=CustomUserCreationForm()
  context={
    "form":form
  }
  return render(request, 'registration/signup.html',context)