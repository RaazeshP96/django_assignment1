from django.urls import path, include
from .views import PostList, about_view, PostDetail, PostCreate, PostDelete, PostUpdate, UserPostListView

urlpatterns = [
    path('', PostList.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('<int:pk>/', PostDetail.as_view(), name='blog-detail'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='blog-delete'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='blog-update'),
    path('new/', PostCreate.as_view(), name='blog-create'),
    path('about/', about_view, name='blog-about')
]
