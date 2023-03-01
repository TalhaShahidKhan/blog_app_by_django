from django.urls import path
from blog.views import listing_post,post_details,create_post,update_post,delt_post,add_comment,upd_comment,delt_comment
urlpatterns = [
    path('',listing_post,name='post_list'),
    path('post/add/',create_post,name='post_add'),
    path('post/<str:slug>/',post_details,name='post_det'),
    path('post/upd/<str:slug>/',update_post,name='post_upd'),
    path('post/dlt/<str:slug>/',delt_post,name='post_dlt'),
    path('post/<str:slug>/com/',add_comment,name='post_addcom'),
    path('post/<str:slug>/com/<int:pk>/upd/',upd_comment,name='post_updcom'),
    path('post/<str:slug>/com/<int:pk>/dlt/',delt_comment,name='post_dltcom'),
]

app_name="blog"