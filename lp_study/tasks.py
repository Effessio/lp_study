from __future__ import absolute_import

from mds.models import Item
from lp_study.celery import app
from time import sleep


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def all_quantity():
    sleep(50)
    return sum([item.quantity for item in Item.objects.all()])
