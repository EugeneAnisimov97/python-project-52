from django.test import TestCase
from django.urls import reverse
from task_manager.users.models import User
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


# Create your tests here.
class UserTests(TestCase):
    fixtures = ['labels.json', 'tasks.json', 'users.json', 'statuses.json']

    def setUp(self):
        pass

    def test_users_index(self):
        response = self.client.get(reverse('users_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/index.html')
        self.assertContains(response, 'first2 last2')
        self.assertContains(response, 'first1 last1')
        self.assertContains(response, 'deleteme please')
        self.assertEqual(len(response.context['users']), 3)

    def test_create_user(self):
        response = self.client.post(reverse('users_create'), {
            'first_name': 'Eugene',
            'last_name': '2',
            'username': 'eugene1',
            'password1': 'Qwas1997',
            'password2': 'Qwas1997'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='eugene1').exists())

    def test_logout(self):
        self.client.force_login(get_user_model().objects.get(pk=1))
        response = self.client.post(reverse('logout'), follow=True)
        self.assertRedirects(response, reverse('index'))

    def test_update_users(self):
        response = self.client.get(
            reverse('users_update', kwargs={'pk': 2}),
            follow=True
        )
        self.assertRedirects(response, reverse('login'))
        self.assertContains(
            response, _("You are not logged in! Please log in.")
        )
        self.client.force_login(get_user_model().objects.get(pk=1))
        response = self.client.get(
            reverse('users_update', kwargs={'pk': 2}),
            follow=True
        )
        self.assertRedirects(response, reverse('users_index'))
        self.assertContains(
            response, _("You don't have permissions to modify another user.")
        )
        response = self.client.get(
            reverse('users_update', kwargs={'pk': 1}),
            follow=True
        )
        self.assertTemplateUsed(response, 'form.html')
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse('users_update', kwargs={'pk': 1}), {
                'first_name': '1to2',
                'last_name': '1to22',
                'username': '111to222',
                'password1': 'Qwas1997',
                'password2': 'Qwas1997'
            },
            follow=True
        )
        self.assertRedirects(response, reverse('users_index'))
        self.assertContains(response, _('User successfully changed'))
        self.assertEqual(User.objects.get(pk=1).username, "111to222")

    def test_delete_user(self):
        self.client.force_login(get_user_model().objects.get(pk=3))

        response = self.client.get(
            reverse('users_delete', kwargs={'pk': 2}),
            follow=True
        )
        self.assertRedirects(response, reverse('users_index'))
        self.assertContains(
            response, _("You don't have permissions to modify another user.")
        )

        self.client.force_login(get_user_model().objects.get(pk=2))
        response = self.client.post(
            reverse('users_delete', kwargs={'pk': 2}),
            follow=True
        )
        self.assertRedirects(response, reverse('users_index'))
        self.assertContains(
            response, _("Cannot delete a user because it is in use")
        )
        self.assertEqual(User.objects.count(), 3)

        self.client.force_login(get_user_model().objects.get(pk=3))
        user = User.objects.get(pk=3)
        response = self.client.post(reverse(
            'users_delete', args=[user.pk])
        )
        self.assertRedirects(response, reverse('users_index'))
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(pk=user.pk).exists())
