# from django.test import TestCase
# from django.urls import reverse
# from task_manager.users.models import User
# from ..statuses.models import Status


# # Create your tests here.
# class StatusesTests(TestCase):

#     def setUp(self):
#         self.user = User.objects.create_user(username='test', password='test')
#         self.client.login(username='test', password='test')

#     def test_create_status(self):
#         response = self.client.post(
#             reverse('statuses_create'),
#             {'name': 'status'}
#         )
#         self.assertEqual(response.status_code, 302)
#         self.assertTrue(Status.objects.filter(name='status').exists())

#     def test_update_status(self):
#         status = Status.objects.create(name='status')
#         response = self.client.post(
#             reverse('statuses_update',
#                     args=[status.pk]),
#             {'name': 'status1'}
#         )
#         self.assertEqual(response.status_code, 302)
#         status.refresh_from_db()
#         self.assertEqual(status.name, 'status1')

#     def test_delete_status(self):
#         status = Status.objects.create(name='Delete')
#         response = self.client.post(
#             reverse('statuses_delete',
#                     args=[status.pk])
#         )
#         self.assertEqual(response.status_code, 302)
#         self.assertFalse(Status.objects.filter(name='Delete').exists())

#     def test_index_view(self):
#         response = self.client.get(reverse('statuses_index'))
#         self.assertEqual(response.status_code, 200)
