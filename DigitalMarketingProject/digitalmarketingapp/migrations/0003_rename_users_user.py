# Generated by Django 4.0.7 on 2023-03-06 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digitalmarketingapp', '0002_rename_user_users'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
