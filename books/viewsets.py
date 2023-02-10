from django.db.models import Count, Avg
from rest_framework.viewsets import ModelViewSet

from books.models import Book, Author
from books.serializers import BookSerializer, AuthorSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all().select_related('country').prefetch_related('authors')
    serializer_class = BookSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all().annotate(books_count=Count('book'), average_price=Avg('book__price'))
    serializer_class = AuthorSerializer
