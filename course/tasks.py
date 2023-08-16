from datetime import datetime, timedelta

from celery import shared_task

from course.models import Subscription, Course
from django.conf import settings
from django.core.mail import send_mail

from users.models import User


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

@shared_task
def check_deactivate_user():
    """Функция проверяет активность пользователей и деактивирует неактивных"""
    now_time = datetime.now()
    one_month_ago = now_time - timedelta(days=30)
    inactive_users = User.objects.filter(last_login__lt=one_month_ago)
    inactive_users.update(is_active=False)
    print(f'Выявлены следующие неактивные пользователь {inactive_users}')


    #Отправляем сообщение неактивном пользователю
    if inactive_users is not None:
        send_mail(
                subject=f'Деактивация',
                message=f'Вас деактивировали',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[inactive_users.email]
                )