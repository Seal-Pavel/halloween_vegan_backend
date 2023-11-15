# Generated by Django 4.2.7 on 2023-11-15 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('prep_time', models.PositiveIntegerField(help_text='Preparation time in minutes')),
                ('steps', models.TextField(help_text='Step by step instructions')),
                ('ingredients', models.ManyToManyField(related_name='recipes', to='recipes.ingredient')),
            ],
        ),
    ]
