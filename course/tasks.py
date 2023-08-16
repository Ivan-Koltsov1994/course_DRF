from celery import shared_task

from course.models import Subscription, Course
from django.conf import settings
from django.core.mail import send_mail

@shared_task
def send_mail_user_сourse_update(course_id):
    """Функция отправляет синхронную рассылку писем пользователям об обновлении материалов курса"""

    subscribers_list = Subscription.objects.filter(course_id=course_id, status=True)
    course = Course.objects.get(id=course_id)

    for sub in subscribers_list:
        print(f"Отправка сообщения по подписке {sub}")
        send_mail(
            subject=f'Обновление курса {course.name}',
            message=f'Направляем вам новые материалы для курса',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[sub.user.email]
            )


