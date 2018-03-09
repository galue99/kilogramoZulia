from django.test import TestCase
from accounts.models import User

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(first_name="Maryann", last_name="Valero", username="maryann12", password="123123", email="maryannvalerogomez@gmail.com")

