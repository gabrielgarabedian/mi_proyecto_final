from django.urls import path
from blog.views import *

urlpatterns = [
    path('', index, name="index-blog"),
    path('list/', ListPost.as_view(), name="list-post"),
    path('login/', BlogLogin.as_view(), name="blog-login"),
    path('logout/', BlogLogout.as_view(), name="blog-logout"),
    path('search-by-name/', SearchPostByName.as_view(), name="search-by-name-post"),


]