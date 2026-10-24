from django.shortcuts import render,redirect,get_object_or_404
from.models import Book
from.forms import BookForm
# Create your views here.

# View list of books
def book_list(request):
    books = Book.objects.all().order_by('-id')
    return render(request, 'book_list.html', {'books': books})

# Add a book
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form, 'title': 'Add New Book'})

# Update book details
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': form, 'title': 'Edit Book'})

# Delete a book
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book': book})

def book_detail(request,pk):
    book=get_object_or_404(Book,pk=pk)
    return render(request,'book_detail.html',{'book':book})