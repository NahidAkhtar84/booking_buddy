# Generated by Django 3.1.7 on 2021-03-12 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0004_auto_20210312_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
