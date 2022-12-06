from django.db import models

class Music(models.Model):
    title = models.CharField(max_length=10)
    author = models.CharField(max_length=10)
    
    class Meta:
        db_table="music"