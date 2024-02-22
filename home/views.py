from django.shortcuts import render,redirect
from home.forms import CustomUserCreationForm,CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from blog.models import Post
# Create your views here.

User=get_user_model()



def landingpage(request):
  if request.user.is_authenticated:
    return redirect('/home')
  else:
    return render(request, 'home/landingpage.html')

@login_required(login_url='login')
def homepage(request):
  posts = Post.objects.all().order_by('created_at')[0:2]
  context = {
    "posts":posts
  }
  return render(request, 'home/home.html',context)


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



@login_required(login_url='login')
def profileupdate(request,username):
  user=User.objects.get(username=username)
  form=CustomUserChangeForm(instance=user)
  if request.method =='POST':
    form=CustomUserChangeForm(request.POST,instance=user,files=request.FILES)
    if form.is_valid():
      form.save()
      return redirect("/home/profile/")
  context={
    "form":form
  }

  return render(request,'home/updateprof.html',context)


@login_required(login_url='login')
def dltprof(request,username):
  user=User.objects.get(username=username)
  user.delete()
  return redirect("/")




