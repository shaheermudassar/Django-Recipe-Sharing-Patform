# Generated by Django 5.0.3 on 2024-04-02 11:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipies', '0011_alter_like_recipe'),
        ('userauths', '0005_follow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipies',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipies', to='userauths.profile'),
        ),
    ]
