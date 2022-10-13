from api.models import Book
from django_filters import rest_framework as filters


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class BookFilter(filters.FilterSet):
    author = filters.CharFilter(
        field_name="author__last_name",
        lookup_expr='icontains',
    )

    genres = CharFilterInFilter(
        field_name="genres__title",
        lookup_expr="in",
    )

    published_date = filters.DateFromToRangeFilter()

    class Meta:
        model = Book
        fields = ['genres', 'published_date', 'author']
