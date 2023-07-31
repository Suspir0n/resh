from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import signup_view, login_view, logout_view

class TestAccountsUrls(SimpleTestCase):

    def test_signup_url_is_resolves(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func, signup_view)

    def test_login_url_is_resolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login_view)

    def test_logout_url_is_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout_view)