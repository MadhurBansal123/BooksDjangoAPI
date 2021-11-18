from django.urls import path
from .views import books_operation, book_operation_by_id, external_api_operations

urlpatterns = [
    path(r'v1/books', books_operation),
    path(r'v1/books/<int:bookId>', book_operation_by_id),
    path(r'external-books', external_api_operations)
]
