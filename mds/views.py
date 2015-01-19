from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from mds.models import Item


class ItemList(ListView):
    model = Item


class LowQuantity(ListView):
    model = Item
    queryset = Item.low_quantity_objects.all()
    template_name = 'mds/item_list.html'


def increase_count(request, pk):
    item = Item.objects.get(id=pk)
    item.quantity += 1
    item.save()
    return HttpResponseRedirect('/')