from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models  import Books
from .serializers import BooksSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    