from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category-detail", kwargs={"pk": self.pk})


class WebArchive(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    detail = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("archive-detail", kwargs={"pk": self.pk})
