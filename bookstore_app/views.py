from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookstore_app/book_list.html', {'books': books})

@login_required
def add_to_cart(request, book_id):
    cart = request.session.get('cart', [])
    if book_id not in cart:
        cart.append(book_id)
        request.session['cart'] = cart
    return redirect('book_list')


@login_required
def view_cart(request):
    cart = request.session.get('cart', [])
    books = Book.objects.filter(id__in=cart)
    return render(request, 'bookstore_app/cart.html', {'books': books})
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('book_list')
        else:
            return render(request, 'bookstore_app/login.html', {'error': 'Invalid credentials'})
    return render(request, 'bookstore_app/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')