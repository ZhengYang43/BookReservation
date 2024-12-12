from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    year = models.CharField(max_length=20, choices=[('Sophomore', 'Sophomore'), ('Junior', 'Junior'), ('Senior', 'Senior')])
    gpa = models.FloatField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    STATUS_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    currently_checked_out = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
        default='No'
    )
    number_of_times_checked_out = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Reservation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reserved_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'book')
