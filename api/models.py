from django.db import models

class Students(models.Model):
    Name = models.CharField(max_length=50,null=False)
    RollNumber = models.PositiveIntegerField(unique=True,null=False)
    DateofBirth = models.DateField(auto_now=False, auto_now_add=False,null=False)

class StudentMarks(models.Model):
    Marks = models.PositiveIntegerField(null=False)
    StudID = models.ForeignKey(Students, on_delete=models.CASCADE,related_name='StudentKa')
    Grade = models.CharField(max_length=2)