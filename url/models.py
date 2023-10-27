from django.db import models

# Create your models here.
class URL(models.Model):
    long_url = models.URLField(max_length=2048)
    short_code = models.UUIDField(unique=True)