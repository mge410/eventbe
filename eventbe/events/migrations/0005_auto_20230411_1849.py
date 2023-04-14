# Generated by Django 3.2.17 on 2023-04-11 15:49

from django.conf import settings
from django.db import migrations
from django.db import models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0004_remove_eventthumbnail_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name='organizer',
            ),
        ),
        migrations.AlterField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(to='events.Tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default='000_000', verbose_name='slug'),
        ),
        migrations.DeleteModel(
            name='EventThumbnail',
        ),
    ]