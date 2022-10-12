from django.urls import path
from api import views

urlpatterns = [
    path('books/', views.book_list),
    path('books/<int:book_id>/', views.book_detail),
]
