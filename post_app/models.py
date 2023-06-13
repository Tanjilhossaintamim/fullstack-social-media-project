from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_post')
    post_content = models.TextField()
    post_image = models.ImageField(upload_to='post_images')
    publish_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_at']

    def __str__(self):
        return self.post_content


class Follow(models.Model):
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follow_user')
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following_user')
    
    


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_comment')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='post_comment')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-comment_date']

    def __str__(self):
        return self.comment


class Like(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_like')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='like_post')
