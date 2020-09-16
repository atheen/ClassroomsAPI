from django.shortcuts import render
from .serializers import UserCreateSerializer,ClassroomSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from classes.models import Classroom,Student

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class ClassroomListView(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
