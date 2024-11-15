from django.test import TestCase
from django.urls import reverse
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class UserTests(TestCase):
    fixtures = ['labels.json', 'tasks.json', 'users.json', 'statuses.json']

    def setUp(self):
        self.status = Status.objects.get(pk=1)

    def test_create_task(self):
        response = self.client.get(reverse('tasks_create'), follow=True)
        self.assertRedirects(response, reverse('login'))
        self.assertContains(
            response, _("You are not logged in! Please log in.")
        )

        self.client.force_login(get_user_model().objects.get(pk=1))
        response = self.client.get(reverse('tasks_create'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form.html')
        response = self.client.post(reverse('tasks_create'), {
            'name': 'Task1',
            'description': 'This is test task',
            'status': self.status.pk,
            'executor': '',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(name='Task1').exists())
        self.assertEqual(Task.objects.count(), 3)

    def test_tasks_index(self):
        response = self.client.get(reverse('tasks_index'), follow=True)
        self.assertRedirects(response, reverse('login'))
        self.assertContains(
            response, _("You are not logged in! Please log in.")
        )

        self.client.force_login(get_user_model().objects.get(pk=1))
        response = self.client.get(reverse('tasks_index'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/index.html')
        self.assertEqual(len(response.context['tasks']), 2)
        self.assertContains(response, "Task 1")
        self.assertContains(response, "Task 2")

    def test_task_detail(self):
        response = self.client.get(
            reverse('tasks_detail', kwargs={"pk": 1}), follow=True
        )
        self.assertRedirects(response, reverse('login'))
        self.assertContains(
            response, _("You are not logged in! Please log in.")
        )

        self.client.force_login(get_user_model().objects.get(pk=1))
        response = self.client.get(
            reverse('tasks_detail', kwargs={"pk": 1}), follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/detail.html')
        self.assertContains(response, "Task 1")
        self.assertContains(response, "first1 last1")
        self.assertContains(response, "first2 last2")
        self.assertContains(response, "with task")

    def test_update_task(self):
        response = self.client.get(
            reverse('tasks_update', kwargs={"pk": 1}), follow=True
        )
        self.assertRedirects(response, reverse('login'))
        self.assertContains(
            response, _("You are not logged in! Please log in.")
        )
        self.client.force_login(get_user_model().objects.get(pk=1))
        response = self.client.get(
            reverse('tasks_update', kwargs={"pk": 1}), follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form.html')
        task = Task.objects.get(pk=1)
        response = self.client.post(
            reverse('tasks_update', args=[task.pk]), {
                'name': 'Task1to2',
                'description': 'newfield',
                'executor': 1,
                'status': 2,
                'labels': 1
            }
        )
        new_task = Task.objects.get(pk=1)
        self.assertRedirects(response, reverse('tasks_index'))
        self.assertEqual(new_task.name, "Task1to2")
        self.assertEqual(response.status_code, 302)

    def test_delete_task(self):
        response = self.client.get(
            reverse('tasks_delete', kwargs={"pk": 1}), follow=True
        )
        self.assertRedirects(response, reverse('login'))
        self.assertContains(
            response, _("You are not logged in! Please log in.")
        )
        self.client.force_login(get_user_model().objects.get(pk=2))
        response = self.client.post(
            reverse('tasks_delete', kwargs={"pk": 1}), follow=True
        )
        self.assertRedirects(response, reverse('tasks_index'))
        self.assertContains(
            response, _("A task can only be deleted by its author.")
        )
        self.assertEqual(Task.objects.count(), 2)
        response = self.client.post(
            reverse('tasks_delete', kwargs={"pk": 2}), follow=True
        )
        self.assertRedirects(response, reverse('tasks_index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Task.objects.count(), 1)
        self.assertContains(response, _('Task successfully deleted'))
