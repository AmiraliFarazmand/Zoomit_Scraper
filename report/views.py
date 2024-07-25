from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

from report.serializers import *
from report.models import Report, Tag
from report.filters import ReportFilter
# Create your views here.

class ReportsListView(ListCreateAPIView):
    serializer_class = ReportSerializer
    queryset = Report.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter, )
    ordering_fields = ("title",)
    search_fields = ("title", "article",)
    # filterset_class = ReportFilter
    
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