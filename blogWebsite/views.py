from django.shortcuts import render, redirect
from blogs.models import Category, Blogs
from .forms import RegistrationForm
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    categories = Category.objects.all()
    featured_post = Blogs.objects.filter(is_published=True)
    posts = Blogs.objects.filter(is_published=False, status='published')
    # print(post)
    
    context = {
        'categories': categories,
        'featured_post': featured_post,
        'posts': posts
    }   
    return render(request, 'home.html', context)


def register(request):
    # Placeholder for registration logic
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally, redirect to a success page or login page
            return redirect('register')  # Redirect to the same page or a different one
    else:
        form = RegistrationForm()
        
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


# Login view
def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')  # Redirect to the dashboard or home page
    else:
        form = AuthenticationForm()
        
    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')