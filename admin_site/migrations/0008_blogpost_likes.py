# Generated by Django 3.1.7 on 2021-03-15 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
