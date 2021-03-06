# Generated by Django 3.2.4 on 2021-10-02 06:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personal_list', '0004_auto_20211002_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(default='avatars/placeholder.png', upload_to='avatars'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='banner',
            field=imagekit.models.fields.ProcessedImageField(default='banners/placeholder.png', upload_to='banners'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='songlist',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
