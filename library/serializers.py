from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['url', 'id', 'title', 'author', 'publication_year', 'genre']

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedIdentityField(view_name='author-books-list', lookup_field='pk')  # Campo de enlace a la lista de libros del autor
    class Meta:
        model = Author
        fields = ['url', 'id', 'name', 'last_name', 'birthdate', 'books']

