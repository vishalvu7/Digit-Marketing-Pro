# Generated by Django 4.0.7 on 2023-03-06 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=35)),
                ('emails', models.EmailField(max_length=35)),
                ('mobiles', models.CharField(max_length=10)),
                ('passwords', models.CharField(max_length=25)),
                ('defaultbalance', models.IntegerField(default=0)),
                ('senderIds', models.CharField(max_length=10)),
            ],
        ),
    ]