from django  import forms
from blog.models import Post


class AddPostForm(forms.ModelForm):
  class Meta:
    model=Post
    fields=["title","content","image"]