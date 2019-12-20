from django.db import models

class News(models.Model):
    title = models.CharField(max_length=150)
    release_date = models.DateField()
    link = models.CharField(max_length=250)
    # file_news = models.FileField(blank=False, null=False)
    def __str__(self):
        return self.title


