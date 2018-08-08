from django.db import models


class ItemModel(models.Model):
    name = models.CharField(max_length=60)
    brand = models.CharField(max_length=60)
    price = models.IntegerField()
    description = models.TextField()
    image = models.URLField()

    def __str__(self):
        return self.name
