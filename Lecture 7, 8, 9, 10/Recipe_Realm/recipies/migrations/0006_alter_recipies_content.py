# Generated by Django 5.0.3 on 2024-04-02 07:47

import django_quill.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipies', '0005_alter_recipies_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipies',
            name='content',
            field=django_quill.fields.QuillField(blank=True, null=True),
        ),
    ]
