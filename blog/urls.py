from django.urls import path, include

from authory.urls import app_name
from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.index,name='index'),
    path('blog/search', views.search, name='search'),
    path('blog/<int:blog_id>', views.blog_view, name='blog_view'),
    path('blog/<pub>',views.public, name='blog_view'),
    path('blog/comment/pub',views.pub_comment,name='pub_comment'),

]