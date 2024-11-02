# Generated by Django 5.1.2 on 2024-11-02 20:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0005_alter_task_executor'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='label',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='labels.label'),
            preserve_default=False,
        ),
    ]
