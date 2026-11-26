from django.db import models

# Create your models here.
from module_management.models import Module


class Lesson(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField(null=True)

    module = models.ForeignKey(Module,on_delete=models.CASCADE)

    slug = models.SlugField(max_length=250,unique=True,null=True)

    order = models.PositiveIntegerField(null=True)

    video_url = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)

    resource_link = models.CharField(max_length=200,null=True)

    duration = models.FloatField()
    

    def __str__(self):
            return f"{self.module.title} - {self.title}"
    
    class Meta:
        ordering = ["order"]
        unique_together = ["module", "order"]