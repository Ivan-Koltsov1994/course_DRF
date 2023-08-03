from rest_framework import serializers

from course.models import Course, Lesson, Paying, Subscription
from course.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [UrlValidator(field='url_video')]  # Проверка требований валидации


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()  # поле вывода количества уроков в курсе
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True, )  # поле вывода уроков курса
    course_status = serializers.SerializerMethodField()  # поле вывода статуса подписки текущего пользователя на курс

    class Meta:
        model = Course
        fields = ('id', 'name', 'preview', 'description', 'lessons', 'lessons_count', 'course_status')

    def get_lessons_count(self, instance):
        # метод определяет количество уроков в курсе
        lessons = Lesson.objects.filter(course=instance).all()
        if lessons:
            return lessons.count()
        return 0

    def get_course_status(self, instance):
        # метод определяет статус подписки пользователя на текущий курс
        user = self.context['request'].user.id
        subscription = Subscription.objects.filter(course=instance, user=user)
        if subscription:
            return subscription.first().status
        return False


class PayingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Paying
        fields = "__all__"


class SubscriptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
