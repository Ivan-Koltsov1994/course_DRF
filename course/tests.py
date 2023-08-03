from rest_framework.test import APITestCase
from rest_framework import status
from course.models import Course, Lesson
from users.models import User, UserRoles


class CourseTestCase(APITestCase):
    """Тестируем эндпоит модели курса"""

    def setUp(self) -> None:
        # Данные тестового пользователя
        self.user = User.objects.create(
            email='test@skypro.com',
            phone='+799999999999',
            city='LA',
            is_superuser=False,
            is_staff=True,
            is_active=True,
            role=UserRoles.MEMBER,
        )
        self.user.set_password('9ol.9OL>((')
        self.user.save()

        # Получаем токен авторизации
        response = self.client.post('/token/', {"email": "test@skypro.com", "password": "9ol.9OL>(("})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # Данные для создания курса
        self.test_data = {
            "name": "test",
            "description": "test",
        }

        self.test_response_data = {'id': 1, 'name': 'test', 'preview': None, 'description': 'test', 'lessons': [],
                                   'lessons_count': 0}

    def test_create_course(self):
        """Тестируем создание Курса"""

        response = self.client.post(
            '/courses/course/',
            data=self.test_data
        )

        # print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_list_course(self):
        """Тестируем получение списка курсов"""

        self.test_create_course()  # создаем экземпляр Курса

        response = self.client.get(
            '/courses/course/'
        )
        # print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'count': 1,
             'next': None,
             'previous': None,
             'results':
                 [{'id': 3, 'name': 'test', 'preview': None, 'description': 'test', 'lessons': [], 'lessons_count': 0}]
             }

        )

    def test_course_get(self):
        """Тестируем получение экземпляра Курса"""
        self.test_create_course()  # создаем экземпляр Курса

        response = self.client.get(
            '/courses/course/1/'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LessonTestCase(APITestCase):
    """Тестируем эндпоит модели урока"""

    def setUp(self) -> None:
        # Данные тестового пользователя
        self.user = User.objects.create(
            email='test@skypro.com',
            phone='+799999999999',
            city='LA',
            is_superuser=False,
            is_staff=True,
            is_active=True,
            role=UserRoles.MEMBER,
        )
        self.user.set_password('9ol.9OL>((')
        self.user.save()

        # Получаем токен авторизации
        response = self.client.post('/token/', {"email": "test@skypro.com", "password": "9ol.9OL>(("})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # Данные для создания урока
        self.test_data = {'name': 'test', 'description': 'test',
                          'video': 'https://www.youtube.com/watch?v=rPp46idEvnM'}
        self.test_response_data = {'id': 2, 'name': 'test', 'preview': None, 'description': 'test', 'url_video': None,
                                   'course': None, 'owner': None}

    def test_lesson_create(self):
        """Тестируем создание Урока"""
        response = self.client.post('/courses/lesson/create/', self.test_data)

        # print(response.json())


        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_get_lesson(self):
        """Тестируем создание экземпляра Курса"""
        self.test_lesson_create()# создаем экземпляр Урока

        response = self.client.get('/courses/lesson/detail/1/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {'id': 1, 'name': 'test', 'description': 'test', 'preview': None, 'url_video': None, 'course': None,
             'owner': None}
        )

    def test_list_lesson(self):
        """Тестируем получение списка уроков"""

        self.test_lesson_create()  # создаем экземпляр Урока

        response = self.client.get(
            '/courses/lesson/'
        )
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'count': 0, 'next': None, 'previous': None, 'results': []}

        )