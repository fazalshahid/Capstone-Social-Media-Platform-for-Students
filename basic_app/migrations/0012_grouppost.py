# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-29 23:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0011_group_grouptable'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('pub_date', models.DateTimeField()),
                ('likes', models.IntegerField(default=0)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group', to='basic_app.Group')),
                ('liked_by', models.ManyToManyField(related_name='group_liked_by', to='basic_app.Profile')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_owner', to='basic_app.Profile')),
            ],
        ),
    ]