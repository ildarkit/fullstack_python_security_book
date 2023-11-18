from django.test import TestCase
from django.contrib.auth import get_user_model


class TestAuthentication(TestCase):

    def test_authenticated_workflow(self):
        passphrase = 'wool reselect resurface annuity'
        get_user_model().objects.create_user('bob', password=passphrase)

        self.client.login(username='bob', password=passphrase)
        self.assertIn('sessionid', self.client.cookies)

        response = self.client.get('/accounts/profile/', secure=True)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'bob')

        self.client.logout()
        self.assertNotIn('sessionid', self.client.cookies)

    def test_prohibit_anonymous_access(self):
        response = self.client.get('/accounts/profile/', secure=True)
        self.assertEqual(302, response.status_code)
        self.assertIn('/accounts/login/', response['Location'])
