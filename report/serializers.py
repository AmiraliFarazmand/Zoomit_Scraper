from rest_framework import serializers
from report.models import Report, Tag



class ReportSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField(method_name="get_tags",)
    # tags = TagSerializer(many=True)
    class Meta:
        model = Report
        fields = ("title", "article", "refrence", "tags",)
    def get_tags(self, obj):
        tags = obj.report_tags.all()
        