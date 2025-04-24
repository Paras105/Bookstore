from django.views import View
from django.shortcuts import render, redirect
from .models import Book

class AdminBookListView(View):
    def get(self, request):
        if not request.user.is_superuser:
            return redirect('book_list')
        books = Book.objects.all()
        return render(request, 'bookstore_app/admin/book_list.html', {'books': books})

class AdminAddBookView(View):
    def get(self, request):
        if not request.user.is_superuser:
            return redirect('book_list')
        return render(request, 'bookstore_app/admin/add_book.html')
    
    def post(self, request):
        if not request.user.is_superuser:
            return redirect('book_list')
        
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        
        # Manual validation
        errors = {}
        if not title:
            errors['title'] = 'Title is required'
        if not author:
            errors['author'] = 'Author is required'
        try:
            price = float(price)
            if price <= 0:
                errors['price'] = 'Price must be greater than zero'
        except (ValueError, TypeError):
            errors['price'] = 'Invalid price'
            
        if not errors:
            Book.objects.create(title=title, author=author, price=price)
            return redirect('admin_book_list')
        return render(request, 'bookstore_app/admin/add_book.html', {'errors': errors})