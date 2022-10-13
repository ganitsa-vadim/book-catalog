from rest_framework import serializers

from api.models import Book, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['title']


class BookSerializerMixin:

    @staticmethod
    def get_genres(book: Book):
        genres = book.genres.all()
        serializer = GenreSerializer(
            instance=genres,
            many=True,
        )
        return serializer.data

    @staticmethod
    def get_author_name(book: Book):
        return book.author.get_full_name()
