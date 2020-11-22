from django.shortcuts import render, get_object_or_404
from .models import blog
# Create your views here.

def all_blogs(request):
    blogs = blog.objects
    return render(request, 'blog/home.html', {'blogs':blogs})

def detail_blog(request, blog_id):
    detail = get_object_or_404(blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'detail':detail})
