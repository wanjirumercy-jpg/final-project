# Generated by Django 4.2.5 on 2024-12-06 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Learn', '0004_skillfeature'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillfeature',
            name='feature_img',
            field=models.ImageField(default='default_image.jpg', upload_to='features/'),
        ),
    ]
