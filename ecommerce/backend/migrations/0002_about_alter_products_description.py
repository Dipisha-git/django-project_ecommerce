# Generated by Django 4.0.2 on 2022-03-19 10:02

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg_image', models.ImageField(upload_to='aboutBgPic')),
                ('content_img', models.ImageField(blank=True, null=True, upload_to='contentPic')),
                ('title', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]