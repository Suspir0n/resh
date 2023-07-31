from django.test import TestCase
from accounts.models import CustomUser


class TestAccountsModels(TestCase):

    def setUp(self):
        self.user_one = CustomUser.objects.create_user(
            username='resh',
            email='resh@gmail.com',
            password='123456',
        )

    def test_custom_user_creation(self):
        self.assertEquals(self.user_one.username, 'resh')

    def test_custom_user_updation(self):
        response = CustomUser.objects.first()

        response.username = 'resh defense'
        response.email = 'reshdefense@gmail.com'
        response.password = '123456'

        response.save()

        self.assertEquals(CustomUser.objects.first().username, 'resh defense')
        self.assertEquals(CustomUser.objects.count(), 1)