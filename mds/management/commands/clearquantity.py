from django.core.management.base import BaseCommand, CommandError
from mds.models import Item


class Command(BaseCommand):
    args = '<item_id item_id ...>'
    help = 'Makes quantity equal to zero to item with item_id'

    def handle(self, *args, **options):
        try:
            item = Item.objects.get(pk=int(args[0]))
            item.quantity = 0
            item.save()
            self.stdout.write('now you don\'t have item {0} in your storage'.format(item.name))
        except Item.DoesNotExist:
            raise CommandError('Item "%s" does not exist' % args[0])
