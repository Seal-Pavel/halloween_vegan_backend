# Generated by Django 4.2.7 on 2024-02-19 20:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_messages', to=settings.AUTH_USER_MODEL),
        ),
    ]
