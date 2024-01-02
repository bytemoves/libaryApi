from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Staff,Student
from .serializers import StudentSerializer,StaffSerializer


class StudentViewSet(viewsets.ModelViewSet):
     queryset = Student.objects.all()
     serializer_class = StudentSerializer
     permission_classes = [IsAuthenticated]
     
     
class StaffSerializer(viewsets.ModelViewSet):
     queryset = Student.objects.all()
     serializer_class = StudentSerializer
     permission_classes = [IsAuthenticated]
    