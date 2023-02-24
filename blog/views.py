from django.shortcuts import render,redirect
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
      form.save()
      
  return render(request, 'blog/addpost.html',context)