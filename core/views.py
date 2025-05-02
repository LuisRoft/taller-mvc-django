from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Author
from .forms import BookForm, AuthorForm

# READ - List
def book_list(request):
    books = Book.objects.all()
    return render(request, 'core/book_list.html', {'books': books})

# READ - Detail
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'core/book_detail.html', {'book': book})

# CREATE
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'core/book_form.html', {'form': form})

# UPDATE
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'core/book_form.html', {'form': form})

# DELETE
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'core/book_confirm_delete.html', {'book': book})


# READ - List
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'core/author_list.html', {'authors': authors})

# READ - Detail
def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'core/author_detail.html', {'author': author})

# CREATE
def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'core/author_form.html', {'form': form})

# UPDATE
def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'core/author_form.html', {'form': form})

# DELETE
def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')
    return render(request, 'core/author_confirm_delete.html', {'author': author})
