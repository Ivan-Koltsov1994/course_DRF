from rest_framework import generics, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from course.models import Course, Lesson, Paying
from course.serializers import CourseSerializer, LessonSerializer, PayingSerializers


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonListView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonCreateView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDeleteView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDetailView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class PayingListView(generics.ListAPIView):
    serializer_class = PayingSerializers
    queryset = Paying.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter,SearchFilter]
    filterset_fields = ['course', 'lesson', 'pay_type']
    search_fields = ['course', 'lesson', 'pay_type']
    ordering_fields = ['pay_date']


class PayingCreateView(generics.CreateAPIView):
    serializer_class = PayingSerializers
    queryset = Paying.objects.all()

class PayingDeleteView(generics.DestroyAPIView):
    serializer_class = PayingSerializers
    queryset = Paying.objects.all()

class PayingDetailView(generics.RetrieveAPIView):
    serializer_class = PayingSerializers
    queryset = Paying.objects.all()

class PayingUpdateView(generics.UpdateAPIView):
    serializer_class = PayingSerializers
    queryset = Paying.objects.all()