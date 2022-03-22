# Generated by Django 4.0.2 on 2022-03-19 16:50

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_about_alter_products_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('mem_image', models.ImageField(blank=True, null=True, upload_to='memberImage')),
                ('position', models.CharField(max_length=255)),
                ('details', ckeditor.fields.RichTextField()),
            ],
        ),
    ]