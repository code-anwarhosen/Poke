# Generated by Django 5.1.4 on 2025-01-14 17:58

import chat.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_alter_chatroom_avatar_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=chat.models.chat_group_avatar_path),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=chat.models.user_avatar_path),
        ),
    ]
