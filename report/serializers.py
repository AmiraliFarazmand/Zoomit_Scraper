from rest_framework import serializers
from report.models import Report, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
        
        
class ReportSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Report
        fields = ("title", "article", "refrence", "tags")

class ReportListSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field='name'
    )
    class Meta:
        model = Report
        fields = ("id", "title", "refrence", "tags")
    
class TagsReportSerializer(serializers.ModelSerializer):
    reports = ReportSerializer(many=True)
    class Meta:
        model = Tag
        fields = ("name", "reports")

