# Generated by Django 5.1.2 on 2024-10-16 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_author_alter_task_executor_alter_task_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='created_at',
        ),
    ]
