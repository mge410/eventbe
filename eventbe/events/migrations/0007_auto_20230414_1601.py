# Generated by Django 3.2.17 on 2023-04-14 13:01

from django.conf import settings
from django.db import migrations
from django.db import models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0006_auto_20230411_1904'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventcomment',
            options={
                'default_related_name': 'comments',
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
        migrations.AlterModelOptions(
            name='eventgallery',
            options={
                'default_related_name': 'event_gallery',
                'verbose_name': 'Event Gallery Photo',
                'verbose_name_plural': 'Event Gallery Photos',
            },
        ),
        migrations.RemoveField(
            model_name='eventthumbnail',
            name='event',
        ),
        migrations.AddField(
            model_name='eventthumbnail',
            name='events',
            field=models.OneToOneField(
                blank=True,
                help_text='main image',
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='event_image',
                to='events.event',
                verbose_name='main image',
            ),
        ),
        migrations.AlterField(
            model_name='eventcomment',
            name='author',
            field=models.ForeignKey(
                help_text='comment author',
                on_delete=django.db.models.deletion.CASCADE,
                related_name='comments',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name='eventcomment',
            name='event',
            field=models.ForeignKey(
                help_text='comment',
                on_delete=django.db.models.deletion.CASCADE,
                related_name='comments',
                to='events.event',
                verbose_name='comment',
            ),
        ),
    ]
