# Generated by Django 3.2.4 on 2021-07-22 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210722_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='embed_link',
        ),
    ]
