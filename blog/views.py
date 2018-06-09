from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.published.all()
    return render (request, 'blog/post/list.html',{'posts':posts})

def post_detail(request, year, month, date, post):
    post = get_object_or_404(Post, slug=post, status='published',publish__year=year,publish__month=month,publish__date=date)
    return render(request,'blog/post/detail.html',{'post':post})