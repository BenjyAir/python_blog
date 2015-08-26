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
        return '%s--%s' % (self.date, self.title, )

    class Meta:
        ordering = ['-date']


class Book(models.Model):
    title = models.CharField(max_length=100)
    isJD = models.BooleanField(blank= False, null=False, default=True)
    jdId = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField()
    url = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

    # class Meta:
    #     ordering = ['-date']

