from django.shortcuts import HttpResponseRedirect
from django.urls import reverse


def index(requset):
    return HttpResponseRedirect(reverse('post_app:all_post'))
