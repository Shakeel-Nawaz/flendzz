from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/student/',views.StudentsAPI.as_view(),name='students'),
    path('api/student/<int:pk>/',views.StudentsAPI.as_view(),name='student'),
    path('api/student/add-mark/',views.MarksAPIVW.as_view(),name='marks'),
    path('api/student/add-mark/<int:pk>/',views.MarksAPIVW.as_view(),name='mark'),
    path('api/student/results/',views.ResultsAPI.as_view(),name='results')
]
