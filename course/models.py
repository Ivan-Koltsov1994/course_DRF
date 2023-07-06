from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    """Класс описания модели курса"""
    name = models.CharField(max_length=150,verbose_name="название курса", **NULLABLE)
    preview =models.ImageField(upload_to="course/",verbose_name="изображение", **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        """Класс мета настроек"""
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ('name')

class Lesson(models.Model):
    """Класс описания модели урока"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='название курса')
    name = models.CharField(max_length=150,verbose_name="название урока", **NULLABLE)
    preview =models.ImageField(upload_to="course/",verbose_name="изображение", **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        """Класс мета настроек"""
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ('name')