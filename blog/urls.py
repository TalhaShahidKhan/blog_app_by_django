from django.urls import path
from blog.views import listing_post,post_details,create_post
urlpatterns = [
    path('',listing_post,name='post_list'),
    path('post/<str:slug>',post_details,name='post_det'),
    path('post/add/',create_post,name='post_add'),
]

app_name="blog"