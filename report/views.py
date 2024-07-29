from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from django.http.response import HttpResponse

from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

from report.serializers import *
from report.models import Report, Tag
from report.webscrapper import add_single_post, extract_some_page
# Create your views here.

class ReportsListView(ListCreateAPIView):
    serializer_class = ReportListSerializer
    queryset = Report.objects.all().order_by("-id")
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter, )
    # ordering_fields = ("title", "id")
    search_fields = ("title", "article")
    
class ReportView(RetrieveAPIView):
    serializer_class = ReportSerializer
    queryset = Report.objects.all()
    
class TagListCreateView(ListCreateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    
class TagReportsView(RetrieveAPIView):
    serializer_class = TagsReportSerializer
    queryset = Tag.objects.all()
    lookup_field = "name"
    
def InsertDataView(request):
    # name = "new4"
    # link = "gg.cc"
    # tags = ["mobile", "new-tag"]
    # article = "lorem ..........................................."
    # add_single_post(name, tags, link, article)
    extract_some_page(1,5)
    return HttpResponse('DONE!!!')