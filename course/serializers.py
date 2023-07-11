from rest_framework import serializers

from course.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMetodField()  # Для модели курса добавили в сериализатор поле вывода

    # количества уроков.

    def get_lesson_count(self, instance):
        # Метод вычисляет количество уроков
        lessons = Lesson.objects.filter(course=instance).all()
        if lessons:
            return lessons.count()
        return 0

    class Meta:
        model = Lesson
        fields = (
            "id",
            "course",
            "name",
            "preview",
            "description",
            "lessons_count",
        )
