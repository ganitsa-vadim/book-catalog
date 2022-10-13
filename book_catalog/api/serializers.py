from rest_framework import serializers

from api.mixins import BookSerializerMixin
from api.models import Book, Review


class BookSerializer(serializers.ModelSerializer, BookSerializerMixin):
    genres = serializers.SerializerMethodField("get_genres")
    author = serializers.SerializerMethodField("get_author_name")
    is_favorite = serializers.SerializerMethodField("check_is_favorite")

    class Meta:
        model = Book
        fields = ['id', 'title', 'genres', 'author', 'average_rating', 'is_favorite']


class BookDetailSerializer(serializers.ModelSerializer, BookSerializerMixin):
    genres = serializers.SerializerMethodField("get_genres")
    author = serializers.SerializerMethodField("get_author_name")
    is_favorite = serializers.SerializerMethodField("check_is_favorite")
    reviews = serializers.SerializerMethodField("get_reviews")

    @staticmethod
    def get_reviews(book: Book):
        reviews = book.reviews.all()
        serializer = ReviewSerializer(
            instance=reviews,
            many=True,
        )
        return serializer.data

    class Meta:
        model = Book
        fields = ['id', 'title', 'genres', 'author', 'average_rating', 'is_favorite', 'reviews']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['author', 'average_rating', 'text']
