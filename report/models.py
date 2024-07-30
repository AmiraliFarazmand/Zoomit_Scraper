from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False, primary_key=True)
    def __str__(self) -> str:
        return self.name
    
class Report(models.Model):
    # change null=True s at the end
    title = models.CharField(max_length=256, null=True, )        
    article = models.TextField(max_length=4096, null=True,)    
    refrence = models.CharField(max_length=512, null=True, )
    tags = models.ManyToManyField(Tag, related_name="reports")
    published_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    def __str__(self) -> str:
        return self.title

