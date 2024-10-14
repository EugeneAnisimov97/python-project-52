from django.test import TestCase
from django.urls import reverse
from task_manager.users.models import User


# Create your tests here.
class UserFormTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='qwerty')

    def test_create_user(self):
        data = {
            'first_name': 'Eugene',
            'last_name': '2',
            'username': 'eugene1',
            'password1': 'Qwas1997',
            'password2': 'Qwas1997'
        }
        response = self.client.post(reverse('users_create'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='eugene1').exists())

    def test_update_user(self):
        self.client.login(username='test', password='qwerty')
        response = self.client.post(reverse(
            'users_update', args=[self.user.id]), {
                'first_name': '1',
                'last_name': '2',
                'username': 'test2',
                'password1': '124',
                'password2': '124'
        })
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'test2')

    def test_delete_user(self):
        self.client.login(username='test', password='qwerty')
        response = self.client.post(reverse(
            'users_delete', args=[self.user.id])
        )
        self.assertRedirects(response, reverse('users_index'))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(id=self.user.id).exists())
