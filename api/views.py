from rest_framework.views import APIView
from rest_framework.response import Response
from .models import StudentMarks, Students
from .serializers import MarksAPI, StudentAPI
from rest_framework import status

#----------------------------/api/student/----------------------------------------#

class StudentsAPI(APIView):
    def get(self,request,pk=None,format=None):
        id = pk
        if id is not None:
            qs = Students.objects.get(id=id)
            sr = StudentAPI(qs)
            return Response(sr.data)
        qs = Students.objects.all()
        sr = StudentAPI(qs,many=True)
        return Response(sr.data)

    def post(self,request,format=None):
        sr = StudentAPI(data=request.data)
        if sr.is_valid():
            sr.save()
            return Response({'Success':'Student Added Successfully'},status=status.HTTP_201_CREATED)
        return Response(sr.errors)

#---------------------------/api/student/add-mark/---------------------------------#

class MarksAPIVW(APIView):
    def get(self,request,pk=None,format=None):
        id = pk
        if id is not None:
            qs = StudentMarks.objects.get(StudID=id)
            sr = MarksAPI(qs)
            return Response(sr.data)
        qs = StudentMarks.objects.all()
        srz = MarksAPI(qs,many=True)
        return Response(srz.data,status=status.HTTP_302_FOUND)

    def post(self,request,pk=None,format=None):
        sr2 = MarksAPI(data=request.data)
        if sr2.is_valid():
            sr2.save()
            return Response({'Success':'Marks Added Successfully'},status=status.HTTP_201_CREATED)
        return Response(sr2.errors)

#--------------------------/api/students/results/-----------------------------------#

class ResultsAPI(APIView):
    def get(self,request,format=None):
        count = StudentMarks.objects.count()
        GdA = StudentMarks.objects.filter(Grade='A').count()
        GdB = StudentMarks.objects.filter(Grade='B').count()
        GdC = StudentMarks.objects.filter(Grade='C').count()
        GdD = StudentMarks.objects.filter(Grade='D').count()
        GdE = StudentMarks.objects.filter(Grade='E').count()
        GdF = StudentMarks.objects.filter(Grade='F').count()
        Distinction = round(int(GdA)/int(count),2)
        FirstClassPercent = round((int(GdB)+int(GdC))/int(count), 2)
        PassPercent = round((int(count)-int(GdF))/int(count) , 2)
        return Response(
            {
            'The total number of students':count,
            'The number of students in Grade A ': GdA,
            'The number of students in Grade B ': GdB,
            'The number of students in Grade C ': GdC,
            'The number of students in Grade D ': GdD,
            'The number of students in Grade E ': GdE,
            'The number of students in Grade F ': GdF,
            'Distinction %':Distinction,
            'First class %':FirstClassPercent,
            'Pass %': PassPercent
        },status=status.HTTP_200_OK)