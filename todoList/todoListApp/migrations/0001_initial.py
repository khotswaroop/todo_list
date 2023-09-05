# Generated by Django 4.1.3 on 2023-09-01 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('time', models.TimeField(auto_now_add=True)),
                ('images', models.ImageField(upload_to='media')),
            ],
        ),
    ]
