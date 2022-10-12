from api.models import Book


class BookSerializerMixin:

    @staticmethod
    def get_genre_title(book: Book):
        return book.genre.title

    @staticmethod
    def get_author_name(book: Book):
        return book.author.get_full_name()
