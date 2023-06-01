from django.urls import path

from .views import BlogHomeView, BlogDetailView, PostCreate, BlogListView, ArchivesListView
from . import views

app_name='blog'


urlpatterns = [
    path('subscribe/', views.subscribe, name='subs'),
    path('', BlogHomeView.as_view(), name='blog_home'),
    path('search/', views.search_results, name='search_results'),
    path('tag/<str:tag>/', BlogListView.as_view(), name='blog_list'),
    path('archives/<int:year>/', ArchivesListView.as_view(), name='archives_list'),
    path('add_post/', PostCreate.as_view(), name='blog_add'),
    path('detail/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),

    path('comment/edit/<int:pk>/', views.comment_edit, name='comment_edit'),
    path('comment/delete/<int:comment_pk>/', views.comment_delete, name='comment_delete'),
]