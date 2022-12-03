from django.db import models

# Create your models here.
class Blog(models.Model):
    author = models.CharField(max_length=10)
    title  = models.CharField(max_length=10)
    text   = models.TextField()
    is_deleted = models.BooleanField(default=False)
    etc    = models.JSONField()

    class Meta:
        db_table = "blogs"