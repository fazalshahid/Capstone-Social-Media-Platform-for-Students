# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 00:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_auto_20171104_0029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='friends',
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
        migrations.AddField(
            model_name='friendship',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendship_creator_set', to='basic_app.Profile'),
        ),
        migrations.AddField(
            model_name='friendship',
            name='friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_set', to='basic_app.Profile'),
        ),
    ]
