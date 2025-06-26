from django.shortcuts import render, redirect, HttpResponse
import blogs
from . models import Blogs, Category, Comment
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.http import HttpResponseRedirect

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
    # comments
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_post
        comment.comment = request.POST.get('comment', '')
        comment.save()
        return HttpResponseRedirect(request.path_info)  # Redirect to the same page to avoid resubmission
    comments = Comment.objects.filter(blog=single_post)
    comment_count = comments.count()
    context = {
        'single_post': single_post,
        'comments': comments,
        'comment_count': comment_count
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