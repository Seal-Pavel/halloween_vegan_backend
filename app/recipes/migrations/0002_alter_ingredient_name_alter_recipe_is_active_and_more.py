# Generated by Django 4.2.7 on 2023-11-24 22:34

import autoslug.fields
from django.db import migrations, models
import app.recipes.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='title', slugify=app.recipes.models.custom_slugify, unique=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='steps',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='tools',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='year',
            field=models.PositiveIntegerField(default=2023),
        ),
    ]
