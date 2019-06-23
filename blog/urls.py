from django.urls import path
from . import views as blog_views
urlpatterns = [
    path('',blog_views.PostListView.as_view(),name="blog_home"),
    path('post/<str:username>',blog_views.UserPostListView.as_view(),name="blog_post_user"),
    path('post/<int:pk>/',blog_views.PostDetailView.as_view(),name='blog_post_detail'),
    path('post/create-new/',blog_views.PostCreateView.as_view(),name='blog_post_create'),
    path('post/<int:pk>/update/',blog_views.PostUpdateView.as_view(),name='blog_post_update'),
    path('post/<int:pk>/delete/',blog_views.PostDeleteView.as_view(),name='blog_post_delete'),
    path('about/',blog_views.about,name="blog_about"),
]