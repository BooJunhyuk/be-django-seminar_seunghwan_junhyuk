"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blogapp import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('admin/', admin.site.urls),
    path('new/', views.new, name = 'new'),
    path('login/', views.login, name = 'login'),
    path('community/', views.community, name = 'community'),
    path('newuser/', views.newuser, name = 'newuser'),
    path('mbtitest/', views.mbtitest, name = 'mbtitest'),
    path('detail/<int:post_id>', views.detail, name = 'detail'),
    path('edit/<int:post_id>', views.edit, name = 'edit'),
    path('delete/<int:post_id>', views.delete, name = 'delete'),
    path('edit_comment/<int:comment_id>', views.edit_comment, name = 'edit_comment'),
    path('delete_comment/<int:comment_id>', views.delete_comment, name = 'delete_comment'),


]
