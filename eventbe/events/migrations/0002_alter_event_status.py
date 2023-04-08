# Generated by Django 3.2.17 on 2023-04-08 19:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
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
                help_text='Event Status',
                max_length=8,
                verbose_name='status',
            ),
        ),
    ]
