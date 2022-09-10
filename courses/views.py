from django.shortcuts import render
from .serializers import CourseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course
from rest_framework import generics

# Create your views here.

# class CoursesList(APIView):
#     def get(self, request):
#         courses = Course.objects.all()
#         data = CourseSerializer(courses, many=True).data
#         return Response(data)

class CoursesList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

