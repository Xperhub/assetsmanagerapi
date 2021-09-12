from rest_framework.test import APITestCase
from backend.models import Asset
from authentications.models import User

class TestModel(APITestCase):

    def test_creates_user(self):
        user = User.objects.create_user('iyandat@gmail.com', 'password123')
        self.assertIsInstance(user,User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.Email, 'iyandat@gmail.com')

        