# Generated by Django 5.0.3 on 2024-04-02 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipies', '0007_alter_recipe_images_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipies',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
