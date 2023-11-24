

from django.db import models

class EmailModel(models.Model):
    to_email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
