import stripe
from rest_framework import generics, viewsets, status
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView

from course.models import Course, Lesson, Paying, Subscription
from course.paginators import CoursePaginator, LessonPaginator
from course.serializers import CourseSerializer, LessonSerializer, PayingSerializers, SubscriptionSerializers
from course.permissions import UserPermissionsModerator, UserPermissionsOwner
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from course.services import create_paying, save_paying
from users.models import UserRoles


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CoursePaginator
    permission_classes = [IsAuthenticated]

    # Выводит список курсов модераторам, владельцам только созданные им курсы
    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.role == UserRoles.MODERATOR or user.is_superuser:
            return Course.objects.all()
        else:
            return Course.objects.filter(owner=user)


class LessonListView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = LessonPaginator
    permission_classes = [IsAuthenticated]

    # Выводит список уроков модераторам, владельцам только созданные им уроки
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
    permission_classes = [IsAuthenticated | UserPermissionsModerator | UserPermissionsOwner]


class LessonUpdateView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [UserPermissionsModerator | UserPermissionsOwner]


class PayingListView(generics.ListAPIView):
    serializer_class = PayingSerializers
    queryset = Paying.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['course', 'lesson', 'pay_type']
    search_fields = ['course', 'lesson', 'pay_type']
    ordering_fields = ['pay_date']
    permission_classes = [UserPermissionsModerator | UserPermissionsOwner]


class PayingCreateView(generics.CreateAPIView):
    serializer_class = PayingSerializers
    queryset = Paying.objects.all()
    permission_classes = [IsAuthenticated]

    # Добавляем создание платежа на сервисе Stripe
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        session = create_paying(
            course=serializer.validated_data['course'],
            user=self.request.user
        )
        serializer.save()
        save_paying(course=serializer.validated_data['course'],
                    user=self.request.user)
        return Response(session['id'], status=status.HTTP_201_CREATED)


class GetPayingView(APIView):
    """Получение информации о платеже с сервиса stripe"""

    def get(self, request, payment_id):
        payment_intent = stripe.PaymentIntent.retrieve(payment_id)
        return Response({
            'status': payment_intent.status, })


# class PayingDeleteView(generics.DestroyAPIView):
#     serializer_class = PayingSerializers
#     queryset = Paying.objects.all()
#     permission_classes = [UserPermissionsOwner]
#
#
# class PayingDetailView(generics.RetrieveAPIView):
#     serializer_class = PayingSerializers
#     queryset = Paying.objects.all()
#     permission_classes = [UserPermissionsModerator | UserPermissionsOwner]
#
#
# class PayingUpdateView(generics.UpdateAPIView):
#     serializer_class = PayingSerializers
#     queryset = Paying.objects.all()
#     permission_classes = [UserPermissionsModerator | UserPermissionsOwner]


class SubscriptionCreateView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializers
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]


class SubscriptionDeleteView(generics.DestroyAPIView):
    serializer_class = SubscriptionSerializers
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]


class SubscriptionUpdateView(generics.UpdateAPIView):
    serializer_class = SubscriptionSerializers
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]
