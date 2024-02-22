from django  import forms
from ckeditor.widgets import CKEditorWidget
from blog.models import Post,Comment


class AddPostForm(forms.ModelForm):
  class Meta:
    model=Post
    fields=["title","content","image"]
    widgets = {
      'title':forms.TextInput(),
      'content':forms.Textarea(attrs={'placeholder':'Post Content','widget':CKEditorWidget}),
      'image':forms.FileInput()
    }




class CommentForm(forms.ModelForm):
  class Meta:
    model=Comment
    fields=["body"]

