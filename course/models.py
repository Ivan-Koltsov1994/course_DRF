from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    """Класс описания модели курса"""
    name = models.CharField(max_length=150, verbose_name="название курса", **NULLABLE)
    preview = models.ImageField(upload_to="course/", verbose_name="изображение", **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Создатель', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        """Класс мета настроек"""
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    """Класс описания модели урока"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='название курса', **NULLABLE)
    name = models.CharField(max_length=150, verbose_name="название урока", **NULLABLE)
    preview = models.ImageField(upload_to="course/", verbose_name="изображение", **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    url_video = models.URLField(verbose_name='ссылка на видео', **NULLABLE)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Создатель', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        """Класс мета настроек"""
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Paying(models.Model):
    """Класс описания модели Платежей"""

    # Установим флаги со способом оплаты
    CASH = 'cash'
    TRANSFER = 'transfer'
    PAY_TYPE = [
        (CASH, 'cash'),
        (TRANSFER, 'transfer')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    pay_date = models.DateField(auto_now_add=True, verbose_name='дата платежа', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='оплаченный урок', **NULLABLE)
    pay_sum = models.PositiveIntegerField(verbose_name='сумма платежа', **NULLABLE)
    pay_type = models.CharField(choices=PAY_TYPE, max_length=30, default=CASH, verbose_name='способ оплаты', **NULLABLE)

    def __str__(self):
        return f'{self.user} - оплата курса (урока) {self.course if self.course else self.lesson}'

    class Meta:
        """Класс мета настроек"""
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

class Subscription(models.Model):
    """Класс описания модели статуса подписки пользователя"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='наименование курса')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    status = models.BooleanField(default=True, verbose_name='статус подписки')

    class Meta:
        """Класс мета настроек"""
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'