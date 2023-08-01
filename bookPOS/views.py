from django.shortcuts import render, get_object_or_404

from bookPOS.models import Book, Sales, salesItems, Returns

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookPOS/book_list.html', {'books' : books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookPOS/book_detail.html', {'book' : book})
