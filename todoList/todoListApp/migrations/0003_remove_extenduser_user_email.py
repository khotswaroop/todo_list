# Generated by Django 3.2.21 on 2023-09-05 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoListApp', '0002_extenduser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extenduser',
            name='user_email',
        ),
    ]
