from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from api.models import Book
from api.serializers import BookSerializer, BookDetailSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    permission_classes = [IsAuthenticated]
