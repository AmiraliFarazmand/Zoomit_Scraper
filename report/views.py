from django_filters.rest_framework import DjangoFilterBackend
from django.http.response import HttpResponse
from rest_framework.generics import  ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from report.serializers import *
from report.models import Report, Tag
from report.webscrapper import extract_some_page, extract_first_page


class ReportsListView(ListAPIView):
    serializer_class = ReportListSerializer
    queryset = Report.objects.all().order_by("-published_date")
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    ordering_fields = ("published_date",)
    search_fields = ("title", "article")
    

class ReportView(RetrieveAPIView):
    serializer_class = ReportSerializer
    queryset = Report.objects.all()

    
class TagListCreateView(ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

    
class TagReportsView(RetrieveAPIView):
    serializer_class = TagsReportSerializer
    queryset = Tag.objects.all()
    lookup_field = "name"

    
def InsertDataView(request):
    extract_some_page(1,3)
    # extract_first_page()
    return HttpResponse('DONE!!!')