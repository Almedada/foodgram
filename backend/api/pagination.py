from rest_framework.pagination import PageNumberPagination
from django.conf import settings


class MyPageNumberPaginator(PageNumberPagination):
    page_size = getattr(settings, 'PAGE_SIZE', 6)
    page_size_query_param = 'limit'
