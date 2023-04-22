# Generated by Django 3.2.17 on 2023-04-21 20:09

from django.db import migrations
from django.db import models

import events.models


class Migration(migrations.Migration):
    dependencies = [
        ('events', '0013_auto_20230419_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventgallery',
            name='image',
            field=models.ImageField(
                help_text='Will be rendered at 300x300 px',
                upload_to=events.models.EventGallery.saving_path,
                validators=[events.models.validate_image_size],
                verbose_name='image',
            ),
        ),
        migrations.AlterField(
            model_name='eventthumbnail',
            name='image',
            field=models.ImageField(
                help_text='Will be rendered at 300x300 px',
                upload_to=events.models.EventThumbnail.saving_path,
                validators=[events.models.validate_image_size],
                verbose_name='image',
            ),
        ),
    ]
