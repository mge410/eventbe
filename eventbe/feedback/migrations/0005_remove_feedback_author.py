# Generated by Django 3.2.17 on 2023-04-16 06:39

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('feedback', '0004_alter_feedback_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='author',
        ),
    ]