from django.urls import path
from blog.views import listing_post,post_details,create_post,update_post,delt_post
urlpatterns = [
    path('',listing_post,name='post_list'),
    path('post/<str:slug>',post_details,name='post_det'),
    path('post/add/',create_post,name='post_add'),
    path('post/upd/<str:slug>',update_post,name='post_upd'),
    path('post/add/<str:slug>',delt_post,name='post_dlt'),
]

app_name="blog"