# core/views.py

from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Student
from .serializers import StudentSerializer,UserSerializer
from .permissions import IsAdminOrReadOnly
from students.tasks import send_welcome_email  # Import the Celery task
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        student = serializer.save()
        
        # Asynchronously send the welcome email
        send_welcome_email.delay(student.id)
    @action(detail=False,methods=['get'])
    def see_user_name(self,request):
        querry=User.objects.filter(is_active=True)
        serializer=UserSerializer(querry,many=True)
        return Response(serializer.data)
    
    @action(detail=False,methods=['post'])
    def enter_user_in_the_database(self,request):

        serializer=UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)



