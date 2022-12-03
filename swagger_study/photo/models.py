from django.db import models

class Photo(models.Model):
    name = models.CharField(max_length=10)
    blog = models.ForeignKey("blog.Blog", on_delete=models.CASCADE)

    class Meta:
        db_table="photo"