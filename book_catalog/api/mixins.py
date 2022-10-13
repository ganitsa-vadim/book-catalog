from rest_framework import serializers

from api.models import Book, Genre
from users.models import User


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

    def check_is_favorite(self, book: Book):
        user: User = self.context.get('user')
        users_added_to_favorite = book.added_to_favorite.all()
        print(user)
        if user in users_added_to_favorite:
            return True
        return False
