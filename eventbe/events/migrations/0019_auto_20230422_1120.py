# Generated by Django 3.2.17 on 2023-04-22 08:20

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):
    dependencies = [
        ('events', '0018_remove_tag_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=tinymce.models.HTMLField(
                help_text='Describe your event', verbose_name='description'
            ),
        ),
        migrations.AlterField(
            model_name='event',
            name='is_published',
            field=models.BooleanField(
                default=False, verbose_name='is published'
            ),
        ),
    ]
