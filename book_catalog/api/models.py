# from django.db import models
#
#
# class Author(models.Model):
#     pass
#
#
# class Genre(models.Model):
#     pass
#
#
# class Book(models.Model):
#     title = models.CharField(60, null=False)
#     genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     published = models.DateField()
#     user = models.ManyToManyField("users.User", related_name="favorites")
#
#
# class Reviews(models.Model):
#     pass
