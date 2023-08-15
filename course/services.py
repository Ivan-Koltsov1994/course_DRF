import requests

from config import settings
from course.models import Paying

api_key = settings.STRIPE_SECRET_KEY
headers = {'Authorization': f'Bearer {api_key}'}
base_url = 'https://api.stripe.com/v1'


def create_paying(course,user):
    """Метод запрашивает данные с сервиса об осуществлении платежа с сервиса stripe"""
    data = [
        ('amount', course.price*100),
        ('currency', 'rub'),
    ]
    # Запрашиваем данные с сервиса
    response = requests.post(f'{base_url}/payment_intents', headers=headers, data=data)
    if response.status_code != 200:
        raise Exception(f'ошибка осуществления платежа: {response.json()["error"]["message"]}')
    return response.json()


def save_paying(course, user):
    """Функция заносит данные о платеже в базу данных с сервиса stripe"""
    Paying.objects.create(
        user=user,
        course=course,
        pay_sum=course.price,
    )
