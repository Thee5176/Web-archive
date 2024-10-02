from django.db import models
from django.urls import reverse


class Catagory(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class WebArchive(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField()
    category = models.ForeignKey(Catagory, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("archive-detail", kwargs={"pk": self.pk})
