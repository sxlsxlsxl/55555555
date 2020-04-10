from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'pg'
    page_size_query_param = 'pgs'
    max_page_size = 1