from django.db import models

# Create your models here.
class news(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    tags = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.ImageField(upload_to='', null=True)
    author = models.CharField(max_length=50)
    date = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'news'    
