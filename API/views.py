from .serializers import UserCreateSerializer, ClassroomSerializer, ClassroomDetailsSerializer, \
    CreateUpdateClassroomSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView
from classes.models import Classroom, Student


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class ClassroomListView(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer


class ClassroomDetailsView(RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomDetailsSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'


class ClassroomCreateView(CreateAPIView):
    serializer_class = CreateUpdateClassroomSerializer

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)


class ClassroomUpdateView(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = CreateUpdateClassroomSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'


class ClassroomDeleteView(DestroyAPIView):
    queryset = Classroom.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'
