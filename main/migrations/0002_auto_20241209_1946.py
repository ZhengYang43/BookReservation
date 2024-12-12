from django.db import migrations


def load_initial_data(apps, schema_editor):

    Student = apps.get_model("main", "Student")
    Book = apps.get_model("main", "Book")

    import pandas as pd
    import os
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    student_data_path = os.path.join(BASE_DIR,  'data', 'student_data.csv')
    book_data_path = os.path.join(BASE_DIR,  'data', 'book_data.csv')

    student_data = pd.read_csv(student_data_path)
    book_data = pd.read_csv(book_data_path)

    for _, row in student_data.iterrows():
        Student.objects.create(
            first_name=row["firstname"],
            last_name=row["lastname"],
            major=row["major"],
            year=row["year"],
            gpa=row["gpa"]
        )

    for _, row in book_data.iterrows():
        Book.objects.create(
            title=row["bookname"],
            author=row["authorname"],
            currently_checked_out=row["currentlycheckedout"],
            number_of_times_checked_out=row["numberoftimescheckedout"]
        )


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_initial_data),
    ]
