from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework import viewsets, generics

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Authors': reverse('author-list', request=request, format=format),
        'Books': reverse('book-list', request=request, format=format),
        'Authors_Before_A_Year': reverse('authors_before_a_year', kwargs={'year': 'year'}, request=request, format=format),
        'Books_By_Genre': reverse('books-by-genre', kwargs={'genre': 'genre'}, request=request, format=format)

    })

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset= Book.objects.all()
    serializer_class = BookSerializer

class AuthorBookList(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        author_id = self.kwargs['pk']
        return Book.objects.filter(author_id=author_id)

@api_view(['GET'])
def authors_before_a_year(request, year, format=None):
    authors = Author.objects.filter(birthdate__year__lt=year)
    serializer = AuthorSerializer(authors, many=True, context={'request': request})
    return Response(serializer.data)

authors_before_a_year.__name__ = 'authors_before_a_year'

@api_view(['GET'])
def books_by_genre(request, genre, format=None):
    books = Book.objects.filter(genre=genre)
    serializer = BookSerializer(books, many=True, context={'request': request})
    return Response(serializer.data)