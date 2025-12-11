from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

#concept of custompagination

class CustomPagination(PageNumberPagination):
    page_size = 4
    page_size_query_pram="page_size"
    page_query_param = 'pag_num'
    max_page_size = 4


    def get_pagination_response(self,data):
        return Response ({
            'next':self.get_next_link(),
            'previous':self.get_previous_link(),
            'count':self.page.paginator.count,
            'page_size':self.page_size,
            'results':data
        })