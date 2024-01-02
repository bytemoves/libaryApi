from django.contrib import admin

from django.contrib import admin
from .models import Books

@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'title', 'author', 'category', 'copies')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('category', 'author')


