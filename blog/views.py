from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from blog.models import Post
from django.contrib.auth import get_user_model
from blog.forms import AddPostForm
# Create your views here.

User=get_user_model()


def listing_post(request):
  post=Post.objects.all()
  context={
      "post":post
  }
  return render(request,"blog/postlist.html",context)




def post_details(request,slug):
  post=Post.objects.get(slug=slug)
  context={
    "post":post
  }
  return render(request,'blog/postdetails.html',context)





def create_post(request):
  form=AddPostForm()
  context={
    "form":form
  }
  if request.method =="POST":
    form=AddPostForm(request.POST, request.FILES)
    if form.is_valid():
      post =form.save(commit=False)
      post.author = request.user
      post.save()
      return redirect("/blog")
  return render(request, 'blog/addpost.html',context)








def update_post(request,slug):
  post=Post.objects.get(slug=slug)
  form=AddPostForm(instance=post)
  context={
    "form":form
  }
  if request.method == "POST":
    form=AddPostForm(request.POST, instance=post, files=request.FILES)
    if form.is_valid():
      post =form.save(commit=False)
      post.author = request.user
      post.save()
      return redirect("/blog")

  return render(request, "blog/updatepost.html",context)


def delt_post(request,slug):
  post=Post.objects.get(slug=slug)
  post.delete()
  return render(request, 'blog/dltpost.html')