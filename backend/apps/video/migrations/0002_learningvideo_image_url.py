# Generated by Django 4.0.2 on 2022-03-09 08:06

import apps.video.video
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='learningvideo',
            name='image_url',
            field=models.FileField(default='', upload_to=apps.video.video.upload_to),
        ),
    ]
