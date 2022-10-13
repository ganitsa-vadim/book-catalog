from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.conf import settings
from django.db.models import Avg, CheckConstraint, UniqueConstraint, Q


class Genre(models.Model):
    title = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=150, null=False)
    last_name = models.CharField(max_length=150, null=False)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return self.get_full_name()


class Book(models.Model):
    title = models.CharField(max_length=150, null=False)
    description = models.TextField(null=True)
    published_date = models.DateField(null=False)
    # genre = models.ForeignKey(Genre, related_name='books', on_delete=models.CASCADE)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre, related_name='books')

    @property
    def average_rating(self):
        return self.bookrating_set.all().aggregate(Avg('rate'))['rate__avg']

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(null=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reviews', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)

    @property
    def average_rating(self):
        return self.reviewrating_set.all().aggregate(Avg('rate'))['rate__avg']

    def __str__(self):
        return self.text


class BookRating(models.Model):
    rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            CheckConstraint(check=Q(rate__range=(0, 10)), name='boo_valid_rate'),
            UniqueConstraint(fields=['user', 'book'], name='book_rating_once'),
        ]


class ReviewRating(models.Model):
    rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            CheckConstraint(check=Q(rate__range=(0, 10)), name='review_valid_rate'),
            UniqueConstraint(fields=['user', 'review'], name='review_rating_once'),
        ]
