from django.urls import path
from rest_framework.routers import DefaultRouter

from course.views import CourseViewSet, LessonListView, LessonCreateView, LessonDetailView, LessonUpdateView, \
    LessonDeleteView

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


    ] + router.urls