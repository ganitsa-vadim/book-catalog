from api import views
from django.urls import path


urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>/', views.BookDetail.as_view()),
    path('books/<int:pk>/add-to-favorite/', views.AddToFavoritesView.as_view()),
]
