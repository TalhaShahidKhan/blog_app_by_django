from django.db import models
from django.template.defaultfilters import slugify  
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
User=get_user_model()

class Post(models.Model):
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
        return reverse("article_detail", kwargs={"slug": self.slug})  # new

  def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Post,self).save(*args, **kwargs)
  



class Comment(models.Model):
     post=models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
     name=models.CharField(max_length=200)
     body=models.TextField()
     created_on=models.DateTimeField(auto_now_add=True)


     def __str__(self):
          return f"{self.name} on {self.post.title}"
