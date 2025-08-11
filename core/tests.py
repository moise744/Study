from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Student


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class StudentAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.list_url = '/api/students/'

        # Create a non-admin user
        self.user = User.objects.create_user(username='user', password='pass1234')

        # Create an admin user
        self.admin = User.objects.create_superuser(username='admin', password='admin1234')

        # Sample student data
        self.student_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'age': 22
        }

        # Create a student
        self.student = Student.objects.create(**self.student_data)

    def test_list_students_as_unauthenticated_user(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_student_as_unauthenticated_user(self):
        response = self.client.post(self.list_url, {
            'name': 'Jane Doe',
            'email': 'jane@example.com',
            'age': 21
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_student_as_non_admin_user(self):
        tokens = get_tokens_for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + tokens['access'])

        response = self.client.post(self.list_url, {
            'name': 'Jane User',
            'email': 'janeuser@example.com',
            'age': 20
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_student_as_admin_user(self):
        tokens = get_tokens_for_user(self.admin)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + tokens['access'])

        response = self.client.post(self.list_url, {
            'name': 'Jane Admin',
            'email': 'janeadmin@example.com',
            'age': 20
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 2)
        self.assertEqual(Student.objects.last().name, 'Jane Admin')
