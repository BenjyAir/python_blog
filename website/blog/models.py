from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)
    date = models.DateField()
    content = models.TextField(blank=True, null=True)



    def __str__(self):
        return 'title--%s' % self.title

    class Meta:
        ordering = ['-date']