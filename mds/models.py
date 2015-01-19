from django.db import models


class LowQuantityManager(models.Manager):
    def get_queryset(self):
        return super(LowQuantityManager, self).get_queryset().filter(quantity__lte=10)


class Item(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    quantity = models.IntegerField()

    objects = models.Manager()
    low_quantity_objects = LowQuantityManager()

