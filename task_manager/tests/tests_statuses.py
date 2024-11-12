from django.test import TestCase
from django.urls import reverse
from task_manager.statuses.models import Status
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


# Create your tests here.
class LabelTests(TestCase):
    fixtures = ['labels.json', 'tasks.json', 'users.json', 'statuses.json']

    def setUp(self):
        pass

    def test_create_label(self):
        response = self.client.get(reverse('statuses_create'), follow=True)
        self.assertRedirects(response, reverse('login'))
        self.assertContains(
            response, _("You are not logged in! Please log in.")
        )
        self.client.force_login(get_user_model().objects.get(pk=1))
        response = self.client.get(reverse('statuses_create'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form.html')
        response = self.client.post(
            reverse('statuses_create'),
            {'name': 'new_status'}
        )
        self.assertRedirects(response, reverse('statuses_index'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Status.objects.filter(name='new_status').exists())

    def test_label_index(self):
        response = self.client.get(reverse('statuses_index'), follow=True)
        self.assertRedirects(response, reverse('login'))
        self.assertContains(
            response, _("You are not logged in! Please log in.")
        )
        self.client.force_login(get_user_model().objects.get(pk=1))
        response = self.client.get(reverse('statuses_index'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/index.html')
        self.assertEqual(len(response.context['statuses']), 2)
        self.assertContains(response, "with task")
        self.assertContains(response, "without task")

    def test_update_label(self):
        self.client.force_login(get_user_model().objects.get(pk=2))
        status = Status.objects.get(pk=1)
        response = self.client.get(reverse('statuses_update',
                                           args=[status.pk]),
                                   follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form.html')
        response = self.client.post(
            reverse('statuses_update', args=[status.pk]),
            {'name': 'updatedstatus'}
        )
        self.assertRedirects(response, reverse('statuses_index'))
        self.assertEqual(response.status_code, 302)
        status.refresh_from_db()
        self.assertEqual(status.name, 'updatedstatus')

    def test_delete_label(self):
        self.client.force_login(get_user_model().objects.get(pk=2))
        label = Status.objects.get(pk=2)
        response = self.client.post(reverse('statuses_delete',
                                            args=[label.pk]),
                                    follow=True)
        self.assertRedirects(response, reverse('statuses_index'))
        self.assertFalse(Status.objects.filter(pk=label.pk).exists())
        label = Status.objects.get(pk=1)
        response = self.client.post(reverse('statuses_delete',
                                            args=[label.pk]),
                                    follow=True)
        self.assertRedirects(response, reverse('statuses_index'))
        self.assertTrue(Status.objects.filter(pk=label.pk).exists())
