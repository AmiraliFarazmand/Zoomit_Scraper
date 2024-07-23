from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False,)
    title = models.CharField(max_length=256, null=True, default=None)
    description = models.TextField(max_length=1024, null=True, default=None)
    def __str__(self) -> str:
        return self.name
    
class Report(models.Model):
    title = models.CharField(max_length=256, null=True, )        
    article = models.TextField(max_length=4096, null=True,)    
    refrence = models.CharField(max_length=512, null=True, )
    tags = models.ManyToManyField(Tag, related_name="report_tags")
    def __str__(self) -> str:
        return self.title

