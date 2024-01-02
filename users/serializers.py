from rest_framework import serializers
from .models import Student, Staff

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'student_email', 'username', 'debt', 'balance']

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['staff_id', 'username', 'staff_job_type', 'email']
