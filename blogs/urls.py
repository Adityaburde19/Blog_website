from django.urls import path
from . import views
from .views import blogs

urlpatterns = [
    path('<int:category_id>/', views.posts_by_category, name='posts_by_category'),
    # path('<slug:slug>/', blog_detail, name='blog_detail'),
]
