from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Student, Book, Reservation
from .forms import ReservationForm
from django.core.paginator import Paginator
from django.db.models import Avg

def handle_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')


def handle_logout(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    avg_gpa =  Student.objects.all().aggregate(Avg('gpa')).get('gpa__avg', 0)
    total_students = Student.objects.count()
    stats = {
        'total_students': total_students,
        'avg_gpa': avg_gpa,
    }
    return render(request, 'dashboard.html', {'stats': stats})


@login_required
def student_list(request):
    students = Student.objects.all()
    paginator = Paginator(students, 10)
    page = request.GET.get('page')
    students = paginator.get_page(page)
    return render(request, 'student_list.html', {'students': students})

@login_required
def reserve_book(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            student = form.cleaned_data['student']
            book = form.cleaned_data['book']

            if Reservation.objects.filter(student=student).count() >= 4:
                return render(request, 'reservation.html',
                              {'form': form, 'error': 'Student cannot reserve more than 4 books'})

            Reservation.objects.create(student=student, book=book)
            book.currently_checked_out = True
            book.number_of_times_checked_out += 1
            book.save()

            return redirect('dashboard')
    else:
        form = ReservationForm()
    return render(request, 'reservation.html', {'form': form})

@login_required
def book_list(request):
    books = Book.objects.order_by('-number_of_times_checked_out')
    paginator = Paginator(books, 10)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    return render(request, 'book_list.html', {'books': books})



