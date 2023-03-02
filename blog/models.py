from django.db import models
from django.template.defaultfilters import slugify  
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
User=get_user_model()


class IsOwnerOrReadOnly(models.Model):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def can_edit(self, user):
        return user == self.author



class Post(IsOwnerOrReadOnly):
  author=models.ForeignKey(User,on_delete=models.CASCADE)
  title=models.CharField(max_length=100,unique=True,null=False)
  content=models.TextField()
  slug=models.SlugField(null=True,unique=True)
  image=models.ImageField(upload_to='post/images',null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
      ordering = ['-created_at']

  def __str__(self):
        return self.title
  

  def get_absolute_url(self):
        return reverse("post_details", kwargs={"slug": self.slug})  # new

  def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Post,self).save(*args, **kwargs)
  



class Comment(IsOwnerOrReadOnly):
     author = models.ForeignKey(User, on_delete=models.CASCADE)
     post=models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
     name=models.CharField(max_length=200)
     body=models.TextField()
     created_on=models.DateTimeField(auto_now_add=True)

     class Meta:
      ordering = ['-created_on']

     def __str__(self):
            return self.title
     
     
