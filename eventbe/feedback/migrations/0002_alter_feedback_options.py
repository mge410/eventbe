# Generated by Django 3.2.17 on 2023-04-15 13:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={
                'ordering': ('created_at',),
                'verbose_name': 'feedback',
                'verbose_name_plural': 'feedbacks',
            },
        ),
    ]
