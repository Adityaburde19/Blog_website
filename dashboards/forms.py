from django import forms
from blogs.models import Category, Blogs
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blogs # Assuming you have a model fr blog posts
        fields = ('title', 'category', 'blog_image', 'short_description', 'blog_body', 'status','is_published')
        
class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')
        

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')