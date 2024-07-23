from django.urls import path
from . import views

urlpatterns = [
    path("",views.ReportsListView.as_view(), name="show-reports"),
    path("tags/", views.TagCreateView.as_view(), name = "create-tag"),
]