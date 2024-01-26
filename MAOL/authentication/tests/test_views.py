from django.contrib.auth.models import User
from django.test import TestCase


class RegisterTestCase(TestCase):
    def test_post_valid(self):
        res = self.client.post('/auth/register/', {
            'email': 'testemail@gmail.com',
            'username': 'testuser',
            'password1': 'c0mpl3xP@ssw0rd',
            'password2': 'c0mpl3xP@ssw0rd'
        })

        self.assertRedirects(res, '/auth/login/')
        self.assertTrue(User.objects.filter(username='testuser').exists())
    
    def test_post_invalid(self):
        res = self.client.post('/auth/register/', {
            'email': ''
        })

        # Invalid forms still send a 200
        self.assertEqual(res.status_code, 200)
        self.assertFormError(res, 'form', 'email', 'This field is required.')
        self.assertFalse(User.objects.filter(username='testuser').exists())
    
    def test_get(self):
        res = self.client.get('/auth/register/')
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'register.html')