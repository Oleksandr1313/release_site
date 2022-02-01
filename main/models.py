from distutils.command.upload import upload
from email.policy import default
from django.db import models

class Images(models.Model):
    picture = models.ImageField(blank = True, default = "default.png")
    heading = models.TextField(max_length = 70)

    def __str__(self):
        return f"{self.heading}"