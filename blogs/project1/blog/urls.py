from django.contrib import admin
from django.urls import path,include
from blog.views import home,blogs,blogs2,particular_blog,signup

app_name = 'blog'



urlpatterns = [
  path('',home,name='home'),
  path('blogs/',blogs,name='blogs'),

  path('blogs2/',blogs2,name='blogs2'),
  path('blog/<slug:data>/',particular_blog,name='blog_detail'),
  path('signup/',signup,name='signup')
]