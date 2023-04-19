# Generated by Django 3.2.17 on 2023-04-19 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_useravatar_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useravatar',
            name='user',
            field=models.OneToOneField(blank=True, help_text='user profile picture', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='avatar', to=settings.AUTH_USER_MODEL),
        ),
    ]
