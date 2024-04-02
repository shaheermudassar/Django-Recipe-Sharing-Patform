# Generated by Django 5.0.3 on 2024-04-01 15:39

import django.db.models.deletion
import django_quill.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userauths', '0005_follow'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Categories/Images')),
                ('small_description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Recipies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('short_description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Recipies/Images')),
                ('youtube_url', models.URLField(blank=True, max_length=255, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipies.category')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userauths.profile')),
            ],
            options={
                'verbose_name_plural': 'Recipies',
            },
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', django_quill.fields.QuillField()),
                ('recipi', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='recipies.recipies')),
            ],
            options={
                'verbose_name_plural': 'Descriptions',
            },
        ),
    ]
