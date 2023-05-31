from django.db import models

class NameList(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    linkedin_url = models.URLField()

    def __str__(self):
        return self.name
