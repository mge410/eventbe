# Generated by Django 3.2.17 on 2023-04-14 13:01

from django.conf import settings
from django.db import migrations
from django.db import models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'text',
                    models.TextField(
                        max_length=200, verbose_name='text field'
                    ),
                ),
                (
                    'created_at',
                    models.DateTimeField(
                        auto_now_add=True, verbose_name='created at'
                    ),
                ),
                (
                    'status',
                    models.CharField(
                        choices=[
                            ('c', 'accepted'),
                            ('b', 'processed'),
                            ('a', 'replied'),
                        ],
                        default='c',
                        help_text='Feedback status',
                        max_length=2,
                        verbose_name='status',
                    ),
                ),
                (
                    'author',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name='feedback author',
                    ),
                ),
            ],
            options={
                'verbose_name': 'mail',
                'verbose_name_plural': 'mails',
                'ordering': ('created_at',),
            },
        ),
    ]
