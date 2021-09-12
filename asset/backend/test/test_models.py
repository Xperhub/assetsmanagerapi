from rest_framework.test import APITestCase
from backend.models import Asset

class TestModel(APITestCase):

    def test_creates_asset(self):
        asset = Asset.objects.create('laptop', 'hp pavilion', 'Iyanda')
        self.assertIsInstance(asset, Asset)
        self.assertEqual(asset.asset_name, 'laptop')
        