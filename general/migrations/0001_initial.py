# Generated by Django 3.1.7 on 2021-03-13 12:20

import ckeditor.fields
from django.db import migrations, models
import general.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='about_us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('imgae', models.ImageField(blank=True, null=True, upload_to=general.models.image_path)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]