# Generated by Django 5.0.1 on 2024-01-16 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='saved',
            field=models.BooleanField(default=False),
        ),
    ]
