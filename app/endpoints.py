from django.urls import path

from . import views

urlpatterns = [
    path('api/blog_posts/', views.blog_post_list_api, name='blog_post_list_api'),
    path('api/blog_posts/<int:pk>/', views.blog_post_detail_api, name='blog_post_detail_api'),
    path('api/blog_posts/create/', views.blog_post_create_api, name='blog_post_create_api'),
    path('api/blog_posts/<int:pk>/update/', views.blog_post_update_api, name='blog_post_update_api'),
    path('api/blog_posts/<int:pk>/delete/', views.blog_post_delete_api, name='blog_post_delete_api'),
]