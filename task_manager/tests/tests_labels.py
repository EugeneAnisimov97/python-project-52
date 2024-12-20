from django.test import TestCase
from django.urls import reverse
from task_manager.labels.models import Label
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class LabelTests(TestCase):
    fixtures = ['labels.json', 'tasks.json', 'users.json', 'statuses.json']

    def setUp(self):
        pass

    def test_create_label(self):
        response = self.client.get(reverse('labels_create'), follow=True)
        self.assertRedirects(response, reverse('login'))
        self.assertContains(
            response, _("You are not logged in! Please log in.")
        )
        self.client.force_login(get_user_model().objects.get(pk=1))
        response = self.client.get(reverse('labels_create'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form.html')
        response = self.client.post(
            reverse('labels_create'),
            {'name': 'new_label'}
        )
        self.assertRedirects(response, reverse('labels_index'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Label.objects.filter(name='new_label').exists())

    def test_label_index(self):
        response = self.client.get(reverse('labels_index'), follow=True)
        self.assertRedirects(response, reverse('login'))
        self.assertContains(
            response, _("You are not logged in! Please log in.")
        )
        self.client.force_login(get_user_model().objects.get(pk=1))
        response = self.client.get(reverse('labels_index'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/index.html')
        self.assertEqual(len(response.context['labels']), 2)
        self.assertContains(response, "with task")
        self.assertContains(response, "without task")

    def test_update_label(self):
        self.client.force_login(get_user_model().objects.get(pk=2))
        label = Label.objects.get(pk=1)
        response = self.client.get(reverse('labels_update',
                                           args=[label.pk]),
                                   follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form.html')
        response = self.client.post(
            reverse('labels_update', args=[label.pk]),
            {'name': 'updatedlabel'}
        )
        self.assertRedirects(response, reverse('labels_index'))
        self.assertEqual(response.status_code, 302)
        label.refresh_from_db()
        self.assertEqual(label.name, 'updatedlabel')

    def test_delete_label(self):
        self.client.force_login(get_user_model().objects.get(pk=2))
        label = Label.objects.get(pk=2)
        response = self.client.post(reverse('labels_delete',
                                            args=[label.pk]),
                                    follow=True)
        self.assertRedirects(response, reverse('labels_index'))
        self.assertFalse(Label.objects.filter(pk=label.pk).exists())
        label = Label.objects.get(pk=1)
        response = self.client.post(reverse('labels_delete',
                                            args=[label.pk]),
                                    follow=True)
        self.assertRedirects(response, reverse('labels_index'))
        self.assertTrue(Label.objects.filter(pk=label.pk).exists())
