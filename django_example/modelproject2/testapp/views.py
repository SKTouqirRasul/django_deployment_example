from django.http import HttpResponse
from django.shortcuts import render
from .models import Author, Tag, Category, Post


def index(request):
    return HttpResponse("Hello Django")


# view function to display a list of posts
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
