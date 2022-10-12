from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request

from api.models import Book
from api.serializers import BookSerializer, BookDetailSerializer


@csrf_exempt
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def book_list(request: Request) -> JsonResponse:
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(
            instance=books,
            many=True,
            context={"user": request.user},
        )
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def book_detail(
        request: Request,
        book_id: int,
):
    if request.method == 'GET':
        book = Book.objects.get(pk=book_id)
        serializer = BookDetailSerializer(book)
        return JsonResponse(serializer.data, safe=False)
