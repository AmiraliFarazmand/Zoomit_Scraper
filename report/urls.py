from django.urls import path
from . import views

urlpatterns = [
    path("",views.ReportsListView.as_view(), name="show-reports"),
    path("<int:pk>/",views.ReportView.as_view(), name="report-detail"),
    path("tags/", views.TagListCreateView.as_view(), name = "all-tags"),
    path("tags/<str:name>/", views.TagReportsView.as_view(), name="tag-reports"),
    # path('insert/', views.InsertDataView, name='insert-data'),
]