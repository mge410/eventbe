# Generated by Django 3.2.17 on 2023-04-15 13:56

from django.conf import settings
from django.db import migrations
from django.db import models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0007_auto_20230414_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(
                help_text='Set date & time for your event',
                verbose_name='date & time',
            ),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(
                help_text='Describe your event',
                max_length=300,
                verbose_name='description',
            ),
        ),
        migrations.AlterField(
            model_name='event',
            name='is_offline',
            field=models.BooleanField(
                default=False,
                help_text='Click if the event is offline',
                verbose_name='is offline',
            ),
        ),
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(
                choices=[
                    ('pub', 'public'),
                    ('authonly', 'authorized only'),
                    ('priv', 'private'),
                ],
                default='pub',
                help_text='Set status for your event',
                max_length=8,
                verbose_name='status',
            ),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(
                help_text='Provide a title for your event',
                max_length=40,
                verbose_name='title',
            ),
        ),
        migrations.AlterField(
            model_name='eventcomment',
            name='author',
            field=models.ForeignKey(
                help_text='Comment author',
                on_delete=django.db.models.deletion.CASCADE,
                related_name='comments',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name='eventcomment',
            name='event',
            field=models.ForeignKey(
                help_text='commented event',
                on_delete=django.db.models.deletion.CASCADE,
                related_name='comments',
                to='events.event',
                verbose_name='comment',
            ),
        ),
        migrations.AlterField(
            model_name='eventcomment',
            name='message',
            field=models.TextField(
                help_text='Your comment',
                max_length=100,
                verbose_name='comment',
            ),
        ),
    ]
