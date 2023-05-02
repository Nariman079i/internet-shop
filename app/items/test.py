from PIL import Image
from django.urls import reverse
from rest_framework.test import APITestCase
from support.models import *


class ItemTest(APITestCase):
    def setUp(self):
        self.url = reverse('support-create')
        self.image = Image.open(r'C:\Users\1\Desktop\test.png')
        self.image.name = "test"
        self.image.format = "PNG"

        self.item = Item.objects.create(
            title="Hello",

            price=10000
        )

    def test_support_create(self):
        res = self.client.post(self.url, {
            'surname': 'Ибрагимов',
            'name': 'Нариман',
            'patronymic': "Ибрагимович",
            'tel': '9829392323',
            'address': "г Махачкала ул Магомеда Гаджиева 196",
            'item': 1
        })
        print(self.image)
        self.assertEqual(res.status_code, 201)
