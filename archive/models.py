from django.db import models


class Catagory(models.Model):
    name = models.CharField(max_length=30)


class WebArchive(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField()
    tag = models.ForeignKey(Catagory, on_delete=models.CASCADE)
