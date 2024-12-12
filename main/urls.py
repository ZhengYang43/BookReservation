from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.handle_login, name='login'),
    path('logout/', views.handle_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('students/', views.student_list, name='student_list'),
    path('books/', views.book_list, name='book_list'),
    path('reserve/', views.reserve_book, name='reserve_book'),
]