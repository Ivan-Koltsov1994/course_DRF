from rest_framework import serializers

from course.models import Course, Lesson, Paying


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField() #  поле вывода количества уроков в курсе
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True,)#  поле вывода уроков курса

    class Meta:
        model = Course
        fields = ('id', 'name', 'preview', 'description', 'lessons', 'lessons_count')

    def get_lessons_count(self, instance):
        # метод определяет количество уроков в курсе
        lessons = Lesson.objects.filter(course=instance).all()
        if lessons:
            return lessons.count()
        return 0

class PayingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Paying
        fields = "__all__"