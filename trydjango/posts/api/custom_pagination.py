from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

class PostlimitOffetPagination(LimitOffsetPagination):
    default_limit = 2
    # max_limit = 3


class PostPageNumberPagination(PageNumberPagination):
    page_size = 1