from django.shortcuts import render,redirect
from home.forms import CustomUserCreationForm

# Create your views here.
def landingpage(request):
  return render(request, 'home/landingpage.html')



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