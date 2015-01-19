from django.core.management.base import BaseCommand
from django.db.models import Max
from mds.models import Item


class Command(BaseCommand):
    help = 'Adds ten more items to database'

    def handle(self, *args, **options):
        max_id = Item.objects.aggregate(Max('id'))['id__max']
        for i in range(10):
            item = Item(name='item{0}'.format(max_id+i), description='no description', quantity=10)
            item.save()
        self.stdout.write('Successfully added ten more items')
