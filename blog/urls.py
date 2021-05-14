from django.urls import path
from . import views
from .feeds import LatestPostsFeed

urlpatterns = [
     path('', views.post_list, name='home'),
     path('search/', views.post_search, name='Post_Search'),

     path('<slug:slug>/', views.post_detail, name='post_detail'),
     path('share/<int:post_id>/', views.shar_post, name='share_post'),
     path('ContactUs/', views.ContactUs ,name='Contactus'),
     path('feed/',LatestPostsFeed(), name = 'post_feed'),
     path('same_post_tag/<slug:tag_slug>/', views.same_post_tag, name='same_post_tag'),
]
