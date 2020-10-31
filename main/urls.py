from django.urls import path
import main.views

# endpoints
urlpatterns = [
    path("books", main.views.BookListView.as_view(), name='book_list'),
    path("books/<int:pk>", main.views.BookDetailView.as_view(), name='book_detail'),
    path('users', main.views.UserListView.as_view(), name='user_list'),
    path('users/new', main.views.UserCreateView.as_view(), name='user_create')
]