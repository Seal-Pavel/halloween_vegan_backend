# Generated by Django 4.2.7 on 2024-02-14 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_remove_recipe_ingredients_remove_recipe_steps_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='ingredients_json',
            new_name='ingredients',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='steps_json',
            new_name='steps',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='tools_json',
            new_name='tools',
        ),
    ]
