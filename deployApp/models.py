from django.db import models


class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title