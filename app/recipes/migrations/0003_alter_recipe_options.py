# Generated by Django 4.2.7 on 2024-02-16 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipe_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'permissions': [('can_choose_winners', 'Может выбрать победителей'), ('can_publish', 'Может публиковать рецепты'), ('can_unpublish', 'Может снимать рецепты с публикации')]},
        ),
    ]
