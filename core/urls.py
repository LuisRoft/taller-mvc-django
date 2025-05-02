from django.urls import path

from . import views

urlpatterns = [
       # Books
    path('', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/create/', views.book_create, name='book_create'),
    path('book/<int:pk>/edit/', views.book_update, name='book_update'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),

    # Authors
    path('authors/', views.author_list, name='author_list'),
    path('author/create/', views.author_create, name='author_create'),
    path('author/<int:pk>/', views.author_detail, name='author_detail'),
    path('author/<int:pk>/edit/', views.author_update, name='author_update'),
    path('author/<int:pk>/delete/', views.author_delete, name='author_delete'),
]
