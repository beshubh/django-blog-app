from django.urls import path
from .views import PostListView, PostDetailView,CreatPostView,UpdatePostView,PostDelteView,UserPostListView
from . import views

urlpatterns = [
    path('',PostListView.as_view(),name='blog-home'),
    path('<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('new/',CreatPostView.as_view(),name='post-create'),
    path('<int:pk>/update/',UpdatePostView.as_view(),name='post-update'),
    path('<int:pk>/delete/',PostDelteView.as_view(),name='post-delete'),
    path('user/<str:username>',UserPostListView.as_view(),name='user-posts'),
    path('about/',views.about,name='blog-about'),
]