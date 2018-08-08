from .models import ItemModel
from scrapy_with_django.celery import app


@app.task
def added_item(item):
    ItemModel.objects.get_or_create(item)
