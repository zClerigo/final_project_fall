# Generated by Django 4.2 on 2024-01-12 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artist', '0001_initial'),
        ('song', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='top_songs',
            field=models.ManyToManyField(to='song.song'),
        ),
    ]
