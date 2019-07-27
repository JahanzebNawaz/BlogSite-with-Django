from django.conf.urls import url
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about', views.AboutView.as_view(), name='about'),
    path('post/<int: pk>', views.DetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int: pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int: pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<int:pk>/commet/', views.add_comment_to_post, name='add'),
]
