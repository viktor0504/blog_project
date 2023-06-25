from django.urls import path

from .views import (BlogHomeView, 
                    PostDetailView, 
                    PostCreate, 
                    BlogListView, 
                    ArchivesListView,
                    PostDeleteView, 
                    PostUpdateView)
from . import views

app_name='blog'


urlpatterns = [
    path('subscribe/', views.subscribe, name='subs'),
    path('search/', views.search_results, name='search_results'),

    path('comment/edit/<int:pk>/', views.comment_edit, name='comment_edit'),
    path('comment/delete/<int:comment_pk>/', views.comment_delete, name='comment_delete'),

    path('archives/<int:year>/', ArchivesListView.as_view(), name='archives_list'),
    path('', BlogHomeView.as_view(), name='blog_home'),
    path('tag/<str:tag>/', BlogListView.as_view(), name='blog_list'),

    path('detail/<slug:slug>/', PostDetailView.as_view(), name='blog_detail'),
    path('add_post/', PostCreate.as_view(), name='add_post'),
    path('delete/<slug:slug>/', PostDeleteView.as_view(), name='delete_post'),
    path('update/<slug:slug>/', PostUpdateView.as_view(), name='update_post'),
]