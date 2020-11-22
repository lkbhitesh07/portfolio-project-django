from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail_blog, name='detail_blog'),
]