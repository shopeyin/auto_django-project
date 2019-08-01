from django.test import TestCase,Client
from django.urls import reverse
from account.models import Account, MyAccountManager
import json

class TestViews(TestCase):


    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.account_url = reverse('account')
        self.must_authenticate_url = reverse('must_authenticate')


    def test_register_GET(self):

        response = self.client.get(self.register_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'account/register.html')


    def test_login_GET(self):
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'account/login.html')

    
    # def test_account_GET(self):
    #     response = self.client.get(self.account_url)

    #     self.assertEquals(response.status_code,200)
    #     self.assertTemplateUsed(response,'account/account.html')

    def test_logout_GET(self):
        response = self.client.get(self.logout_url)

        self.assertEquals(response.status_code,302)
        self.assertTemplateUsed('home')


    
    def test_authenticate_GET(self):
        response = self.client.get(self.must_authenticate_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'account/must_authenticate.html')


    # def test_register_POST_new_user(self):
    #     url = reverse('')
    #     response = self.client.post(self.register_url,{
    #         'email' :'j@y.com',
    #         'username' : 'joy',
    #         'firstname' : 'j',
    #         'lastname' : 'jola',
    #         'phonenumber' : '07083383089',
    #         'address' : 'ikeja',
    #         'raw_password' : 'shopeyin69' ,
    #         'password1' : 'shopeyin69' 
    #     })
    #     self.assertEquals(response.status_code,200)
    #     self.assertTemplateUsed('home')







