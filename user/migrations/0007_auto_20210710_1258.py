# Generated by Django 3.0.7 on 2021-07-10 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20210710_1241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='genre',
            new_name='gender',
        ),
    ]
