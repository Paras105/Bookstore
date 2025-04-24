from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book

class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'bookstore_app/book_list.html', {'books': books})

class LoginView(View):
    def get(self, request):
        return render(request, 'bookstore_app/login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('book_list')
        return render(request, 'bookstore_app/login.html', {'error': 'Invalid credentials'})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, book_id):
        cart = request.session.get('cart', [])
        if book_id not in cart:
            cart.append(book_id)
            request.session['cart'] = cart
        return redirect('book_list')
class RegisterView(View):
    def get(self, request):
        return render(request, 'bookstore_app/register.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})
        
        User.objects.create_user(username=username, password=password)
        return redirect('login')    

class CartView(LoginRequiredMixin, View):
    def get(self, request):
        cart = request.session.get('cart', [])
        books = Book.objects.filter(id__in=cart)
        total = sum(book.price for book in books)
        return render(request, 'bookstore_app/cart.html', {'books': books, 'total_price': total})
class AdminAddBookView(LoginRequiredMixin, View):
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
        cover_image = request.POST.get('cover_image', '')
        
        # Manual validation
        errors = {}
        if not title:
            errors['title'] = 'Title required'
        if not author:
            errors['author'] = 'Author required'
        try:
            price = float(price)
            if price <= 0:
                errors['price'] = 'Price must be positive'
        except (ValueError, TypeError):
            errors['price'] = 'Invalid price'
            
        if not errors:
            Book.objects.create(
                title=title,
                author=author,
                price=price,
                cover_image=cover_image
            )
            return redirect('admin_book_list')
        return render(request, 'bookstore_app/admin/add_book.html', {'errors': errors})
    
class AdminBookListView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.is_superuser:
            return redirect('book_list')
        books = Book.objects.all()
        return render(request, 'bookstore_app/admin/book_list.html', {'books': books})