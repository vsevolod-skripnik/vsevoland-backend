from django.conf import settings
from rest_framework.pagination import PageNumberPagination


class DefaultPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = settings.MAX_PAGE_SIZE
