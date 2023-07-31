from rest_framework.pagination import PageNumberPagination

class CoursePaginator(PageNumberPagination):

    page_size = 2 # Количество элементов на странице
    page_size_query_param = 'page_size'  # Параметр запроса для указания коли
    max_page_size = 50  # Максимальное количество элементов на странице

class LessonPaginator(PageNumberPagination):

    page_size = 2 # Количество элементов на странице
    page_size_query_param = 'page_size'  # Параметр запроса для указания коли
    max_page_size = 50  # Максимальное количество элементов на странице