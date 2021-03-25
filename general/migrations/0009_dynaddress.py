# Generated by Django 3.1.7 on 2021-03-20 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0008_about_us_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='dynAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(blank=True, max_length=255)),
                ('address_2', models.CharField(blank=True, max_length=255)),
                ('zip_code', models.IntegerField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, default='0', max_digits=9)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, default='0', max_digits=9)),
            ],
            options={
                'verbose_name_plural': 'addresses',
            },
        ),
    ]