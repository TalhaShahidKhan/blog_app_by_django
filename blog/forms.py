from django  import forms
from blog.models import Post,Comment


class AddPostForm(forms.ModelForm):
  class Meta:
    model=Post
    fields=["title","content","image"]




class CommentForm(forms.ModelForm):
  class Meta:
    model=Comment
    fields=["name","body"]