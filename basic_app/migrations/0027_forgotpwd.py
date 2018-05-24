# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-25 20:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0026_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForgotPwd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=150, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic_app.Profile')),
            ],
        ),
    ]
