from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blog.models import Post,Comment
from django.contrib.auth import get_user_model
from blog.forms import AddPostForm,CommentForm
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




@login_required(login_url='login')
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







@login_required(login_url='login')
def update_post(request,slug):
  post=Post.objects.get(slug=slug)
  form=AddPostForm(instance=post)
  context={
    "form":form,
  }
  if not post.can_edit(request.user):
        messages.error(request,"You don't have permission to update others post")
        return redirect('/blog')
  if request.method == "POST" :
    form=AddPostForm(request.POST, instance=post, files=request.FILES)
    if form.is_valid():
      post =form.save(commit=False)
      post.author = request.user
      post.save()
      return redirect("/blog")

  return render(request, "blog/updatepost.html",context)

@login_required(login_url='login')
def delt_post(request,slug):
  post=Post.objects.get(slug=slug)
  if not post.can_edit(request.user):
        messages.error(request,"You don't have permission to delete others post")
        return redirect('/blog')
  else:
    post.delete()
  return render(request, 'blog/dltpost.html')




@login_required(login_url='login')
def add_comment(request,slug):
  post=Post.objects.get(slug=slug)
  form=CommentForm()
  context={
    "form":form,
    "post":post
  }
  
  if request.method == "POST":
    form=CommentForm(request.POST)
    if form.is_valid():
      obj=form.save(commit=False)
      obj.author=request.user
      obj.post=post
      obj.save()
      return redirect("/blog")
  return render(request, 'blog/addcomments.html',context )



@login_required(login_url='login')
def upd_comment(request,slug,pk):
  post=Post.objects.get(slug=slug)
  comment=Comment.objects.get(id=pk)
  form=CommentForm(instance=comment)
  context={
    "form":form,
    "post":post,
    "comment":comment,
  }
  if not comment.can_edit(request.user):
        messages.error(request,"You don't have permission to update other's comment")
        return redirect('/blog')
  if request.method == "POST" :
    form=CommentForm(request.POST,instance=comment)
    if form.is_valid():
      obj=form.save(commit=False)
      obj.post=post
      obj.save()
      return redirect("/blog")
  return render(request, 'blog/updatecomments.html',context )

@login_required(login_url='/login')
def delt_comment(request,slug,pk):
  post=Post.objects.get(slug=slug)
  comment=Comment.objects.get(id=pk)
  if not comment.can_edit(request.user):
        messages.error(request,"You don't have permission to delete other's comment")
        return redirect('/blog')
  else:
    comment.delete()
  return redirect("/blog")