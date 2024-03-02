from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog_post_list, name='blog_post_list'),
    path('<int:pk>/', views.blog_post_detail, name='blog_post_detail'),
    path('create/', views.blog_post_create, name='blog_post_create'),
    path('<int:pk>/update/', views.blog_post_update, name='blog_post_update'),
    path('<int:pk>/delete/', views.blog_post_delete, name='blog_post_delete'),
    path('api/blog_posts/', views.blog_post_list_api, name='blog_post_list_api'),
    path('api/blog_posts/<int:pk>/', views.blog_post_detail_api, name='blog_post_detail_api'),
    path('api/blog_posts/create/', views.blog_post_create_api, name='blog_post_create_api'),
    path('api/blog_posts/<int:pk>/update/', views.blog_post_update_api, name='blog_post_update_api'),
    path('api/blog_posts/<int:pk>/delete/', views.blog_post_delete_api, name='blog_post_delete_api'),
]