from rest_framework import serializers

from api.mixins import BookSerializerMixin
from api.models import Book
from users.models import User


class BookSerializer(serializers.ModelSerializer, BookSerializerMixin):
    genre = serializers.SerializerMethodField("get_genre_title")
    author = serializers.SerializerMethodField("get_author_name")
    is_favorite = serializers.SerializerMethodField("check_is_favorite")

    def check_is_favorite(self, book: Book):
        user: User = self.context.get('user')
        users_added_to_favorite = book.added_to_favorite.all()
        if user in users_added_to_favorite:
            return True
        return False

    class Meta:
        model = Book
        fields = ['id', 'title', 'genre', 'author', 'average_rating', 'is_favorite']


class BookDetailSerializer(serializers.ModelSerializer, BookSerializerMixin):
    genre = serializers.SerializerMethodField("get_genre_title")
    author = serializers.SerializerMethodField("get_author_name")

    class Meta:
        model = Book
        fields = ['id', 'title', 'genre', 'author', 'average_rating']
