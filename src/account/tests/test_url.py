from django.test import SimpleTestCase
from django.urls import reverse, resolve
from account.views import registration_view, login_view,account_view,logout_view,must_authenticate_view

class TestUrls(SimpleTestCase):
    
    def test_updateaccount_url_is_resolves(self):
        url = reverse('account')
        print(resolve(url))
        self.assertEquals(resolve(url).func,account_view)

    def test_register_url_is_resolves(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func,registration_view)

    def test_login_url_is_resolves(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func,login_view)

    def test_logout_url_is_resolves(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func,logout_view)


    def test_authenticate_url_is_resolves(self):
        url = reverse('must_authenticate')
        print(resolve(url))
        self.assertEquals(resolve(url).func,must_authenticate_view)

