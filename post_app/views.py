from typing import Any, Dict
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
# Create your views here.


class UserPost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = UserPostForm
    template_name = 'post_app/post_form.html'
    context_object_name = 'form'

    def form_valid(self, form: BaseModelForm):
        post_user = form.save(commit=False)
        post_user.user = self.request.user
        post_user.save()
        return HttpResponseRedirect(reverse('post_app:all_post'))


class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post_app/all_post.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        posts = context['posts']
        for post in posts:
            already_like = Like.objects.filter(
                user=self.request.user, post=post)
            if already_like:
                like = True
            else:
                like = False
            context['like'] = like

        return context


@login_required
def post_details(request, id):
    post = Post.objects.get(pk=id)
    comment_form = CommentForm()
    all_comments = Comment.objects.filter(post=post)
    already_like = Like.objects.filter(user=request.user, post=post)
    if already_like:
        like = True
    else:
        like = False

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('post_app:post_details', kwargs={'id': id}))
    return render(request, 'post_app/post_details.html', context={'post': post, 'comment_form': comment_form, 'all_comments': all_comments, 'like': like})


@login_required
def like(request, id):
    post = Post.objects.get(pk=id)
    already_like = Like.objects.filter(user=request.user, post=post)
    if not already_like:
        Like.objects.create(user=request.user, post=post)
    return HttpResponseRedirect(reverse('post_app:post_details', kwargs={'id': post.pk}))


@login_required
def unlike(request, id):
    post = Post.objects.get(pk=id)
    already_like = Like.objects.filter(user=request.user, post=post)
    if already_like:
        already_like.delete()
    return HttpResponseRedirect(reverse('post_app:post_details', kwargs={'id': post.pk}))


@login_required
def user_details(request, id):
    current_user = User.objects.get(pk=id)
    posts = Post.objects.filter(user=id)

    already_follow = Follow.objects.filter(
        follower=current_user, following=request.user)
    if already_follow:
        followed = True
    else:
        followed = False

    return render(request, 'login/profile_details.html', context={'current_user': current_user, 'posts': posts, 'followed': followed})


@login_required
def add_follow(request, id):
    follow_request_user = User.objects.get(pk=id)
    already_follow = Follow.objects.filter(
        follower=follow_request_user, following=request.user)

    if not already_follow:
        Follow.objects.create(follower=follow_request_user,
                              following=request.user)

    return HttpResponseRedirect(reverse('post_app:profile_details', kwargs={'id': id}))


@login_required
def unfollow(request, id):
    follow_request_user = User.objects.get(pk=id)
    follower = Follow.objects.get(
        follower=follow_request_user, following=request.user)
    if follower:
        follower.delete()
        return HttpResponseRedirect(reverse('post_app:profile_details', kwargs={'id': id}))


@login_required
def user_post(request):
    posts = Post.objects.filter(user=request.user)
    if posts:
        user_post = True
        dic = {
            'posts': posts,
            'user_post': user_post
        }
        for post in posts:
            already_like = Like.objects.filter(user=request.user, post=post)
            if already_like:
                like = True
                dic.update({'like': like})

            else:
                like = False
                dic.update({'like': like})

    else:
        dic = {}
        user_post = False
        dic.update({'user_post': user_post})

    return render(request, 'post_app/my_post.html', context=dic)


class EditPost(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['post_image', 'post_content']
    template_name = 'post_app/edit_post.html'
    context_object_name = 'form'

    def form_valid(self, form: BaseModelForm):
        post_form = form.save(commit=False)
        post_form.user = self.request.user
        post_form.save()
        return HttpResponseRedirect(reverse('post_app:userpost'))

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['post_id'] = self.object.pk
        return context


def delete_post(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return HttpResponseRedirect(reverse('post_app:userpost'))
