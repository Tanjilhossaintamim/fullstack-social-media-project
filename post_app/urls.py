from django.urls import path
from . import views


app_name = 'post_app'
urlpatterns = [
    path('create_post/', views.UserPost.as_view(), name='create_post'),
    path('all_post/', views.PostList.as_view(), name='all_post'),
    path('post_details/<int:id>/', views.post_details, name='post_details'),
    path('like/<int:id>/', views.like, name='like'),
    path('unlike/<int:id>/', views.unlike, name='unlike'),
    path('profile_details/<int:id>/', views.user_details, name='profile_details'),
    path('add_follow/<int:id>/', views.add_follow, name='add_follow'),
    path('unfollow/<int:id>/', views.unfollow, name='unfollow'),
    path('userpost/', views.user_post, name='userpost'),
    path('edit_post/<pk>/',views.EditPost.as_view(),name='edit_post'),
    path('delete_post/<int:id>/',views.delete_post,name='delete_post')
]
