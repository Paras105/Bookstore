from django.urls import path
from .views import (
    BookListView, LoginView, LogoutView,
    AddToCartView, CartView, AdminBookListView
)

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add-to-cart/<int:book_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartView.as_view(), name='view_cart'),
    path('admin/books/', AdminBookListView.as_view(), name='admin_book_list'),
]