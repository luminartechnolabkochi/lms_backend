from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.response import Response

from course_management.models import Course
from course_management.serializers import CourseSerializer

from accounts.permissions import IsOwner


class CourseListCreateView(ListAPIView,CreateAPIView):
  
    authentication_classes =[authentication.TokenAuthentication]

    permission_classes =[permissions.IsAuthenticated]

    serializer_class = CourseSerializer

    def get_queryset(self):
        return Course.objects.filter(trainer = self.request.user)

    def perform_create(self, serializer):
        serializer.save(trainer = self.request.user)

   


class CourseRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    queryset = Course.objects.all()
    
    serializer_class = CourseSerializer

    authentication_classes =[authentication.TokenAuthentication]

    permission_classes =[IsOwner]

  