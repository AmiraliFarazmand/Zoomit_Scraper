from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

from report.serializers import *
from report.models import Report, Tag
# Create your views here.

# class ReportsListView(ListAPIView):
#     serializer_class = ReportSerializer
#     queryset = Report.objects.all()

class ReportsListView(ListCreateAPIView):
    serializer_class = ReportSerializer
    queryset = Report.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter, )
    ordering_fields = ("title",)
    search_fields = ("title", "article",)
    

class TagCreateView(ListCreateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()