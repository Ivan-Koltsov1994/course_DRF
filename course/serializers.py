from rest_framework import serializers

from course.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField() #  поле вывода количества уроков в курсе

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons_count(self, instance):
        # метод определяет количество уроков в курсе
        lessons = Lesson.objects.filter(course=instance).all()
        if lessons:
            return lessons.count()
        return 0

class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'