from django.db import models

class Postblog(models.Model):

    STATUS_CHOICES = (
        ('pub', 'Published'),
        ('drf', 'Draft'),
    )
    title = models.CharField(max_length=50)
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)

    def __str__(self):
        return self.title
