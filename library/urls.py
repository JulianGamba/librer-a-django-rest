from django.urls import path, include
from rest_framework.routers import DefaultRouter

from library import views

router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet, basename='author')
router.register(r'books', views.BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
    path('authors/<int:pk>/books/', views.AuthorBookList.as_view(), name='author-books-list'),  # Nueva URL para la lista de libros del autor
    path('authors_before_a_year/<int:year>/', views.authors_before_a_year, name='authors_before_a_year'),
]