from django.test import SimpleTestCase
from django.urls import reverse, resolve
from dashboard.views import dashboard_view, update_user_view, delete_user_view

class TestDashboardsUrls(SimpleTestCase):

    def test_home_url_is_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, dashboard_view)

    def test_update_url_is_resolves(self):
        url = reverse('update', args=['some-email'])
        self.assertEquals(resolve(url).func, update_user_view)

    def test_delete_url_is_resolves(self):
        url = reverse('delete', args=['some-email'])
        self.assertEquals(resolve(url).func, delete_user_view)