from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from mds.models import Item


@receiver(pre_save, sender=Item,)
def my_callback(sender, instance, **kwargs):
    instance.quantity += 2
    print 'not it is gonna be save'


@receiver(post_save, sender=Item)
def my_other_signal(sender, instance, **kwargs):
    print sender.__name__
    print instance.name
    print 'now it has been saved'