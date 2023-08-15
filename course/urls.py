from django.urls import path
from rest_framework.routers import DefaultRouter

from course.views import CourseViewSet, LessonListView, LessonCreateView, LessonDetailView, LessonUpdateView, \
    LessonDeleteView, PayingListView, PayingCreateView,  \
    SubscriptionCreateView, SubscriptionUpdateView, SubscriptionDeleteView, GetPayingView

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns =[
    #Lesson
    path('lesson/', LessonListView.as_view(), name='lesson_list'),
    path('lesson/create/', LessonCreateView.as_view(), name='lesson_create'),
    path('lesson/detail/<int:pk>/', LessonDetailView.as_view(), name='lesson_detail'),
    path('lesson/update/<int:pk>/', LessonUpdateView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>/', LessonDeleteView.as_view(), name='lesson_delete'),

    #Paying
    path('paying/', PayingListView.as_view(), name='paying_list'),
    path('paying/create/', PayingCreateView.as_view(), name='paying_create'),
    path('payment/<str:payment_id>/', GetPayingView.as_view(), name='paying_get'),

    # Subscription
    path('subscription/create/', SubscriptionCreateView.as_view(), name='subscription_create'),
    path('subscription/<int:pk>/update', SubscriptionUpdateView.as_view(), name='subscription_update'),
    path('subscriptions/delete/<int:pk>/', SubscriptionDeleteView.as_view(), name='subscription_delete'),
    ] + router.urls