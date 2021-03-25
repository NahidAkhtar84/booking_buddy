# Generated by Django 3.1.7 on 2021-03-11 15:23

import admin_site.models
import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('details', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('images', models.ImageField(blank=True, null=True, upload_to=admin_site.models.image_path)),
            ],
        ),
    ]