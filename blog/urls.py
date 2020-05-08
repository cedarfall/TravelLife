from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
    path('posts/', PostListView.as_view(), name='posts-home'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    
]
