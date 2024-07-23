from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

from report.serializers import *
from report.models import Report
# Create your views here.

# class ReportsListView(ListAPIView):
#     serializer_class = ReportSerializer
#     queryset = Report.objects.all()

class ReportsListView(ListAPIView):
    serializer_class = ReportSerializer
    queryset = Report.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter, )
    ordering_fields = ("title",)
    search_fields = ("title", "article",)
    