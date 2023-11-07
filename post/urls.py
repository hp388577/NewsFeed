from django.urls import path
from . import views

urlpatterns = [
    path('myfeed/', views.my_feed, name='my-feeds'),
    path('', views.feed, name='feeds'),
    path('feed/', views.feed, name='feed'),
    path('like_post/<int:id>/', views.like_post, name='like-post'),
    path('feed/create/', views.create_feed, name='feed-create'),
    path('feed/edit/<int:id>/', views.edit_feed, name='feed-edit'),
    path('feed/delete/<int:id>/', views.delete_feed, name='feed-delete'),
    path('add-comment/<int:post_id>/', views.add_comment, name='add-comment'),

]