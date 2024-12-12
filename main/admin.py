from django.contrib import admin
from main.models import Student, Book, Reservation

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'major', 'year', 'gpa')
    search_fields = ('first_name', 'last_name', 'major')
    list_filter = ('year', 'major')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'currently_checked_out', 'number_of_times_checked_out')
    search_fields = ('title', 'author')
    list_filter = ('currently_checked_out',)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('student', 'book', 'reserved_date')
    search_fields = ('student__first_name', 'student__last_name', 'book__title')
    list_filter = ('reserved_date',)
