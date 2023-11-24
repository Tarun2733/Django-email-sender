from django.db import models

# Create your models here.
class Emailmodel(models.Model):
    to_email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    file = models.FileField(upload_to='files',blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email