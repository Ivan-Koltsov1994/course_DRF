from django.core.management import BaseCommand

from course.models import Paying


class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Привет! Заполняем базу начальными значениями")
        paying_list = [
    {
        "id": 1,
        "pay_date": "2023-07-12",
        "pay_sum": 1233,
        "pay_type": "cash",
        "user": 1,
        "course": 1,
        "lesson": 1
    },
    {
        "id": 2,
        "pay_date": "2023-07-12",
        "pay_sum": 10000,
        "pay_type": "transfer",
        "user": 1,
        "course": 1,
        "lesson": 3
    }
]

        pay_objects = []
        for item in paying_list:
            pay_objects.append(Paying(**item))

        Paying.objects.bulk_create(pay_objects)