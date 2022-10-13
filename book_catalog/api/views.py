from django.http import JsonResponse
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from api.models import Book
from api.serializers import BookSerializer, BookDetailSerializer
from api.service import BookFilter


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BookFilter


class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    permission_classes = [IsAuthenticated]


class AddToFavoritesView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk: int):
        book = get_object_or_404(Book, pk=pk)
        user = request.user
        user.favorites.add(book)
        return JsonResponse({"status": "true"})
