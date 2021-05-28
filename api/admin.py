from django.contrib import admin
from .models import StudentMarks, Students

@admin.register(Students)
class Student_Details(admin.ModelAdmin):
    list_display = ['id','Name','RollNumber','DateofBirth']

@admin.register(StudentMarks)
class Student_Marks_Details(admin.ModelAdmin):
    list_display = ['id','Marks','Grade']