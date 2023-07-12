from rest_framework import generics, viewsets

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