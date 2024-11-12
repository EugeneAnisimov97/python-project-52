# from django.test import TestCase
# from django.urls import reverse
# from task_manager.tasks.models import Task
# from task_manager.users.models import User
# from task_manager.statuses.models import Status


# # Create your tests here.
# class TasksTests(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='1', password='2')
#         self.status = Status.objects.create(name='New')
#         self.client.login(username='1', password='2')

#     def test_create_task(self):
#         response = self.client.post(reverse('tasks_create'), {
#             'name': 'Test Task',
#             'description': 'This is a test task',
#             'status': self.status.pk,
#             'executor': '',
#         })
#         self.assertEqual(response.status_code, 302)
#         self.assertTrue(Task.objects.filter(name='Test Task').exists())

#     def test_list_tasks(self):
#         self.client.post(reverse('tasks_create'), {
#             'name': 'Test Task',
#             'description': 'This is a test task',
#             'status': self.status.pk,
#             'executor': '',
#         })
#         response = self.client.get(reverse('tasks_index'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Test Task')

#     def test_update_task(self):
#         task = Task.objects.create(
#             name='Old Task',
#             description='This is an old task',
#             status=self.status,
#             author=self.user,
#         )
#         response = self.client.post(reverse('tasks_update', args=[task.pk]), {
#             'name': 'Updated Task',
#             'description': 'This is an updated task',
#             'status': self.status.pk,
#             'executor': '',
#         })
#         self.assertEqual(response.status_code, 302)
#         task.refresh_from_db()
#         self.assertEqual(task.name, 'Updated Task')

#     def test_delete_task(self):
#         task = Task.objects.create(
#             name='Task to Delete',
#             description='This task will be deleted',
#             status=self.status,
#             author=self.user,
#         )
#         response = self.client.post(reverse('tasks_delete', args=[task.pk]))
#         self.assertEqual(response.status_code, 302)
#         self.assertFalse(Task.objects.filter(name='Task to Delete').exists())
