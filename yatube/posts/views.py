from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, template, context) 


def group_posts(request):
    template = 'posts/group_list.html'
    description = 'Это главная страница проекта Yatube'
    context = {
        'description': description,
    }
    return render(request, template, context) 