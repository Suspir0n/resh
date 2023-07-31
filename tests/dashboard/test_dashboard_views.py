from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import CustomUser


class TestDashboardView(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.user = CustomUser.objects.create_user(
            username='resh',
            email='resh@gmail.com',
            password='123456',
        )
        self.client.login(email='resh@gmail.com', password='123456')
        self.update_url = reverse('update', args=[self.user.uuid])
        self.delete_url = reverse('delete', args=[self.user.uuid])

    def test_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['user'], self.user)
        self.assertTemplateUsed(response, 'dashboard/home.html')

    def test_home_UPDATE_custom_user_updation(self):

        new_username = 'resh defense'
        new_email = 'reshdefense@example.com'
        new_password = '123456'

        data = {
            'username': new_username,
            'email': new_email,
            'password': new_password,
        }
        response = self.client.post(self.update_url, data)

        self.assertRedirects(response, reverse('login'))

        self.user.refresh_from_db()

        self.assertEqual(self.user.username, new_username)
        self.assertEqual(self.user.email, new_email)
        self.assertTrue(self.user.check_password(new_password))

    def test_home_DELETE_custom_user_deletion(self):
        response = self.client.delete(self.delete_url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(CustomUser.objects.count(), 0)

