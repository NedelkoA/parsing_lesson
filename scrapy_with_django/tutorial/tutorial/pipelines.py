# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy_with_django.breuninger_shop.tasks import added_item
import sys
import os
import django
from scrapy_with_django.scrapy_with_django.settings import BASE_DIR

sys.path.append(os.path.join(BASE_DIR, 'breuninger_shop'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'breuninger_shop.settings'
django.setup()


class TutorialPipeline(object):
    def process_item(self, item, spider):
        added_item.delay(item)
        print("-----------------------------------------")
        return item
