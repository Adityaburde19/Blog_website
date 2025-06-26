from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from blogs import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('category/', include('blogs.urls')),
    path('blogs/<slug:slug>/', blog_views.blogs, name='blogs'),
    path('blogs/search/', blog_views.search, name='search'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),  # For login, logout, password change, etc.
    path('logout/', views.logout, name='logout'),
    path('dashboard/', include('dashboards.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
