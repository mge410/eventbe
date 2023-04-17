# Generated by Django 3.2.17 on 2023-04-17 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import events.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
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
                    'title',
                    models.CharField(
                        help_text='Provide a title for your event',
                        max_length=40,
                        verbose_name='title',
                    ),
                ),
                (
                    'description',
                    models.TextField(
                        help_text='Describe your event',
                        max_length=300,
                        verbose_name='description',
                    ),
                ),
                (
                    'date',
                    models.DateTimeField(
                        help_text='Set date & time for your event',
                        verbose_name='date & time',
                    ),
                ),
                (
                    'location_x',
                    models.FloatField(null=True, verbose_name='location x'),
                ),
                (
                    'location_y',
                    models.FloatField(null=True, verbose_name='location y'),
                ),
                (
                    'status',
                    models.CharField(
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
                (
                    'created_at',
                    models.DateField(
                        auto_now_add=True, verbose_name='created at'
                    ),
                ),
                (
                    'is_offline',
                    models.BooleanField(
                        default=False,
                        help_text='Click if the event is offline',
                        verbose_name='is offline',
                    ),
                ),
                (
                    'is_active',
                    models.BooleanField(
                        default=True, verbose_name='is active'
                    ),
                ),
                (
                    'is_published',
                    models.BooleanField(
                        default=True, verbose_name='is published'
                    ),
                ),
                (
                    'is_frozen',
                    models.BooleanField(
                        default=False, verbose_name='is frozen'
                    ),
                ),
                (
                    'organizer',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name='organizer',
                    ),
                ),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
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
                    'title',
                    models.CharField(max_length=20, verbose_name='title'),
                ),
                (
                    'slug',
                    models.SlugField(default='000_000', verbose_name='slug'),
                ),
                (
                    'created_at',
                    models.DateField(
                        auto_now_add=True, verbose_name='created at'
                    ),
                ),
                (
                    'is_active',
                    models.BooleanField(
                        default=True, verbose_name='is active'
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='EventThumbnail',
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
                    'image',
                    models.ImageField(
                        help_text='Will be rendered at 300px',
                        upload_to=events.models.EventThumbnail.saving_path,
                        verbose_name='image',
                    ),
                ),
                (
                    'event',
                    models.OneToOneField(
                        blank=True,
                        help_text='event',
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='event_image',
                        to='events.event',
                        verbose_name='event',
                    ),
                ),
            ],
            options={
                'verbose_name': 'event image',
                'verbose_name_plural': 'event images',
                'default_related_name': 'event_image',
            },
        ),
        migrations.CreateModel(
            name='EventGallery',
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
                    'image',
                    models.ImageField(
                        help_text='Will be rendered at 300x300 px',
                        upload_to='saving path',
                        verbose_name='image',
                    ),
                ),
                (
                    'event',
                    models.ForeignKey(
                        blank=True,
                        help_text='gallery images',
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='gallery_images',
                        to='events.event',
                        verbose_name='gallery_images',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Event Gallery Photo',
                'verbose_name_plural': 'Event Gallery Photos',
                'default_related_name': 'gallery_images',
            },
        ),
        migrations.CreateModel(
            name='EventComment',
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
                    'message',
                    models.TextField(
                        help_text='Your comment',
                        max_length=100,
                        verbose_name='comment',
                    ),
                ),
                (
                    'author',
                    models.ForeignKey(
                        help_text='Comment author',
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='comments',
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    'event',
                    models.ForeignKey(
                        help_text='commented event',
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='comments',
                        to='events.event',
                        verbose_name='comment',
                    ),
                ),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
                'default_related_name': 'comments',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(
                help_text='Select appropriate tags for your event',
                related_name='tags',
                to='events.Tag',
            ),
        ),
    ]
