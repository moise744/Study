# students/tasks.py

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from core.models import Student  # Corrected: Import Student from the 'core' app

@shared_task
def test_task(seconds):
    """A simple task to demonstrate Celery functionality."""
    import time
    time.sleep(seconds)
    return f"Waited {seconds} seconds"

@shared_task
def send_welcome_email(student_id):
    """
    Sends a welcome email to a new student.
    Fetches the student object inside the task for reliability.
    """
    try:
        student = Student.objects.get(pk=student_id)
        subject = 'Welcome to the Student Portal!'
        message = f'Hi {student.name}, welcome aboard!'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [student.email]
        
        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=False,
        )
    except Student.DoesNotExist:
        # Log an error or handle the case where the student object is not found
        # You might want to use Django's logging system here
        print(f"Error: Student with ID {student_id} not found for welcome email.")
        pass