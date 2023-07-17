from rest_framework import generics, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from course.models import Course, Lesson, Paying
from course.serializers import CourseSerializer, LessonSerializer, PayingSerializers
from course.permissions import UserPermissionsModerator, UserPermissionsOwner
from rest_framework.permissions import IsAuthenticated

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]

    # Выводит список курсов модераторам, владельцам только созданные им курсы
    def get_queryset(self):
        user = self.request.user
        if request.user.is_staff or request.user.role == UserRoles.MODERATOR or user.is_superuser:
            return Course.objects.all()
        else:
            return Course.objects.filter(owner=user)

class LessonListView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]

    #Выводит список уроков модераторам, владельцам только созданные им уроки
    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser or user.role == UserRoles.MODERATOR:
            return Course.objects.all()
        else:
            return Course.objects.filter(owner=user)

class LessonCreateView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [UserPermissionsOwner]

class LessonDeleteView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [UserPermissionsOwner]

class LessonDetailView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [UserPermissionsModerator | UserPermissionsOwner]

class LessonUpdateView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [UserPermissionsModerator | UserPermissionsOwner]

class PayingListView(generics.ListAPIView):
    serializer_class = PayingSerializers
    queryset = Paying.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter,SearchFilter]
    filterset_fields = ['course', 'lesson', 'pay_type']
    search_fields = ['course', 'lesson', 'pay_type']
    ordering_fields = ['pay_date']
    permission_classes = [UserPermissionsModerator | UserPermissionsOwner]

class PayingCreateView(generics.CreateAPIView):
    serializer_class = PayingSerializers
    queryset = Paying.objects.all()
    permission_classes = [UserPermissionsOwner]

class PayingDeleteView(generics.DestroyAPIView):
    serializer_class = PayingSerializers
    queryset = Paying.objects.all()
    permission_classes = [UserPermissionsOwner]

class PayingDetailView(generics.RetrieveAPIView):
    serializer_class = PayingSerializers
    queryset = Paying.objects.all()
    permission_classes = [UserPermissionsModerator | UserPermissionsOwner]

class PayingUpdateView(generics.UpdateAPIView):
    serializer_class = PayingSerializers
    queryset = Paying.objects.all()
    permission_classes = [UserPermissionsModerator | UserPermissionsOwner]