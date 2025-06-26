from django.shortcuts import render, HttpResponse
import blogs
from . models import Blogs, Category
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.
def posts_by_category(request, category_id):
    # fetch the post that belongs to the category_id
    posts = Blogs.objects.filter(status='published', category_id=category_id)
    # try:
    #     # fetch the category object
    #     category = Category.objects.get(pk=category_id) 
    # except Category.DoesNotExist:
    #     return HttpResponse("Category not found", status=404)
    
    category = get_object_or_404(Category, pk=category_id)    
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'posts_by_category.html', context)


# Blogs
def blogs(request, slug):
    single_post =  get_object_or_404(Blogs, slug=slug, status='published')
    context = {
        'single_post': single_post
    }
    return render(request, 'blogs.html', context)

# serach functionality
def search(request):
    keyword = request.GET.get('keyword', '')
    blogs = Blogs.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='published')
    context = {
        'blogs': blogs,
        'keyword': keyword
    }
    return render(request, 'search.html', context)