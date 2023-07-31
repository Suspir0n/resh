from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import CustomUser


class TestAccountsView(TestCase):

    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signup')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')

    def test_signup_GET(self):
        response = self.client.get(self.signup_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signup.html')

    def test_signup_POST_adds_new_users(self):
        response = self.client.post(self.signup_url, {
            'name_signup': 'resh defense',
            'username_signup': 'resh',
            'email': 'resh@gmail.com',
            'password': '123456',
            'confirm_password': '123456',
        })
        username_count = CustomUser.objects.count()
        username = CustomUser.objects.first().username

        self.assertEquals(response.status_code, 302)
        self.assertEquals(username_count, 1)
        self.assertEquals(username, 'resh')

    def test_signup_POST_no_data(self):
        response = self.client.post(self.signup_url)
        username_count = CustomUser.objects.count()

        self.assertNotEquals(response.status_code, 302)
        self.assertEquals(username_count, 0)

    def test_signup_POST_adds_new_users_with_password_not_equals(self):
        response = self.client.post(self.signup_url, {
            'name_signup': 'resh defense',
            'username_signup': 'resh',
            'email': 'resh@gmail.com',
            'password': '12345678',
            'confirm_password': '123456',
        })
        username_count = CustomUser.objects.count()

        self.assertNotEquals(response.status_code, 302)
        self.assertEquals(username_count, 0)

    def test_signup_POST_adds_new_users_with_password_less_6_characters(self):
        response = self.client.post(self.signup_url, {
            'name_signup': 'resh defense',
            'username_signup': 'resh',
            'email': 'resh@gmail.com',
            'password': '12345',
            'confirm_password': '123456',
        })
        username_count = CustomUser.objects.count()

        self.assertNotEquals(response.status_code, 302)
        self.assertEquals(username_count, 0)

    def test_signup_POST_adds_new_users_exist(self):
        CustomUser.objects.create_user(
            username='resh',
            email='resh@gmail.com',
            password='123456',
        )

        response = self.client.post(self.signup_url, {
            'name_signup': 'resh defense',
            'username_signup': 'resh',
            'email': 'reshdefense@gmail.com',
            'password': '123456',
            'confirm_password': '123456',
        })
        username_count = CustomUser.objects.count()

        self.assertEquals(response.status_code, 302)
        self.assertTrue(CustomUser.objects.filter(username='resh').exists())
        self.assertEquals(username_count, 1)

    def test_login_GET(self):
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_login_POST_auth_users_with_username(self):
        CustomUser.objects.create_user(
            username='resh',
            email='resh@gmail.com',
            password='123456',
        )

        response = self.client.post(self.login_url, {
            'name_or_email_login': 'resh',
            'password': '123456',
        })

        self.assertEquals(response.status_code, 302)

    def test_login_POST_auth_users_with_email(self):
        CustomUser.objects.create_user(
            username='resh',
            email='resh@gmail.com',
            password='123456',
        )

        response = self.client.post(self.login_url, {
            'name_or_email_login': 'resh@gmail.com',
            'password': '123456',
        })

        self.assertEquals(response.status_code, 302)

    def test_login_POST_auth_users_with_username_or_email_error(self):
        user = CustomUser.objects.create_user(
            username='resh',
            email='resh@gmail.com',
            password='123456',
        )

        response = self.client.post(self.login_url, {
            'name_or_email_login': 'reshdefense@gmail.com',
            'password': '123456',
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(CustomUser.objects.count(), 1)
        self.assertNotEquals(user.email, 'reshdefense@gmail.com')

    def test_login_POST_auth_users_with_password_error(self):
        user = CustomUser.objects.create_user(
            username='resh',
            email='resh@gmail.com',
            password='123456',
        )

        response = self.client.post(self.login_url, {
            'name_or_email_login': 'resh@gmail.com',
            'password': '12345678',
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(CustomUser.objects.count(), 1)
        self.assertFalse(user.check_password('12345678'))


    def test_login_POST_no_data(self):
        response = self.client.post(self.login_url)

        self.assertNotEquals(response.status_code, 302)

    def test_logout_GET(self):
        response = self.client.get(self.logout_url)

        self.assertEquals(response.status_code, 302)