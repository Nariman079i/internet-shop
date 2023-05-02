from rest_framework.generics import *
from items.api.seriazlisers import *


class CategoryDetailAPI(RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'slug'


class CategoryListAPI(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ItemListAPI(ListCreateAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class ItemDetailAPI(RetrieveAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    lookup_field = 'id'

