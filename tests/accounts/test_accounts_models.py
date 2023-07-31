from django.test import TestCase
from accounts.models import CustomUser


class TestAccountsModels(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='resh',
            email='resh@gmail.com',
            password='123456',
        )
        self.super_user = CustomUser.objects.create_superuser(
            username='super resh',
            email='superresh@gmail.com',
            password='123456',
        )

    def test_custom_user_creation(self):
        self.assertEquals(self.user.username, 'resh')

    def test_custom_user_creation_without_email(self):
        with self.assertRaises(ValueError) as context:
            CustomUser.objects.create_user(
                username='resh',
                email=None,
                password='123456',
            )
        self.assertEqual(str(context.exception), 'Email is required.')

    def test_custom_super_user_creation(self):
        self.assertEquals(self.super_user.username, 'super resh')

    def test_custom_super_user_creation_with_is_staff_false(self):
        with self.assertRaises(ValueError) as context:
            CustomUser.objects.create_superuser(
                username='super resh1',
                email='superresh1@gmail.com',
                password='123456',
                is_staff=False,
            )
        self.assertEqual(str(context.exception), 'Superuser must have is_staff=True.')

    def test_custom_super_user_creation_with_is_superuser_false(self):
        with self.assertRaises(ValueError) as context:
            CustomUser.objects.create_superuser(
                username='super resh1',
                email='superresh1@gmail.com',
                password='123456',
                is_superuser=False,
            )
        self.assertEqual(str(context.exception), 'Superuser must have is_superuser=True.')

    def test_custom_user_updation(self):
        response = CustomUser.objects.first()

        response.username = 'resh defense'
        response.email = 'reshdefense@gmail.com'
        response.password = '123456'

        response.save()

        self.assertEquals(CustomUser.objects.first().username, 'resh defense')