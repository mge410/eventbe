# Generated by Django 3.2.17 on 2023-04-15 13:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('events', '0008_auto_20230415_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(
                help_text='Select appropriate tags for your event',
                related_name='tags',
                to='events.Tag',
            ),
        ),
    ]