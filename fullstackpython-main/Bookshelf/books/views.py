from django.shortcuts import render , get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from books.forms import ReviewForm
from books.models import Book
# Create your views here.

def book_list(request):
    books = Book.objects.select_related('added_by').annotate(
        avg_rating=Avg('reviews__rating')
    ).order_by('-created_at')
    return render(request, 'books/book_list.html', {'books': books})

def book_details(request, pk):
    book = get_object_or_404(Book,pk=pk)
    reviews = book.reviews.select_related('user').order_by('-created_at')
    avg=reviews.aggregate(avg_rating=Avg('rating'))['avg_rating']
    return render(request, 'books/book_details.html', {
        'book': book, 
        'reviews': reviews, 
        'avg_rating': avg,
    })


@login_required
def add_book(request,pk):
    book = get_object_or_404(Book, pk=pk)
    form = ReviewForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return redirect('book_details', pk=book.pk)
    