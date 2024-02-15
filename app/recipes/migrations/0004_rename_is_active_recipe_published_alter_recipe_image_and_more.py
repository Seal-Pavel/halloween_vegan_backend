# Generated by Django 4.2.7 on 2024-02-15 19:34

import app.recipes.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipe_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='is_active',
            new_name='published',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to=app.recipes.models.upload_to_directory),
        ),
    ]
