from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Book
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.contrib.auth import logout


def search(request):
  query = request.POST.get('query')
  if query:
        books = Book.objects.filter(
         Q(title__icontains=query) |
         Q(authors__name__icontains=query) |
         Q(isbn__icontains=query)
     )
  else:
      books = Book.objects.all()
  return render(request, 'search.html', {'query': query, 'books': books})

def book_details(request, book_id):
   book = get_object_or_404(Book, pk=book_id)
   return render(request, 'book_details.html', {'book': book})

def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})

def register(request):
   if request.method == 'POST':
       form = RegisterForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('login')
   else:
       form = RegisterForm()
   return render(request, 'register.html', {'form': form})

def logout_view(request):
   logout(request)
   return redirect('login')



def genre_books(request, genre):
    books = Book.objects.filter(genre=genre)
    if books.exists():
        genre_display = books.first().get_genre_display()
    else:
        genre_display = genre.title() 
    return render(request, 'genre_search.html', {'books': books, 'genre': genre_display})