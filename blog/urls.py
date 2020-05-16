from django.urls import path
# we need to import views file
# coz we are gonna use functions from that file
from . import views
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView,
    PostDeleteView, UserPostListView#, PostListAPIView)
)

# urlpatterns = [
#     path('<parth of url>',<function from views>,<name of path>)
# ]

urlpatterns = [
    #path('api/post/',PostListAPIView.as_view(),name='post-api'),
    path('',PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail'),
    path('post/new/',PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('user/<str:username>',UserPostListView.as_view(),name='user-post'),
    path('about/',views.about,name='blog-about'),
]