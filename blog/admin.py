from django.contrib import admin
from blog.models import Post,Comment
from django.template.defaultfilters import slugify  

# Register your models here.



class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "content",)
    prepopulated_fields = {"slug": ("title",)}







admin.site.register(Post, PostAdmin)


admin.site.register(Comment)