from django.shortcuts import render , get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.db.models import Avg
from .models import Book, Review
from .forms import BookForm, ReviewForm

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
def add_review(request,pk):
    book = get_object_or_404(Book, pk=pk)
    form = ReviewForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return redirect('book_details', pk=book.pk)
        return render(request, 'books/add_review.html', {'form': form, 'book': book})
    
class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/add_book.html'
    success_url = reverse_lazy('book_list')

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)