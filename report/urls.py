from django.urls import path
from . import views

urlpatterns = [
    path("",views.ReportsListView.as_view(), name="show-reports"),
    
]