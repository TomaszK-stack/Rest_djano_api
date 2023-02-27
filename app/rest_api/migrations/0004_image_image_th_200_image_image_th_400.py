# Generated by Django 4.1.7 on 2023-02-26 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0003_remove_image_user_image_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_th_200',
            field=models.ImageField(blank=True, upload_to='static/thumbnail_200'),
        ),
        migrations.AddField(
            model_name='image',
            name='image_th_400',
            field=models.ImageField(blank=True, upload_to='static/thumbnail_400'),
        ),
    ]
