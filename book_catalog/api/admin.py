from api import models
from django.contrib import admin


admin.site.register(models.Book)
admin.site.register(models.Review)
admin.site.register(models.Author)
admin.site.register(models.Genre)
admin.site.register(models.BookRating)
admin.site.register(models.ReviewRating)
