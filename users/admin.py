from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'username', 'student_email', 'debt', 'balance')
    search_fields = ('username', 'student_id', 'student_email')
from .models import Staff

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('staff_id', 'username', 'staff_job_type', 'email')
    search_fields = ('username', 'staff_id', 'email')