# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-02 03:52
from __future__ import unicode_literals

import django.contrib.postgres.fields.hstore
import django.db.models.deletion
from django.contrib.postgres.operations import HStoreExtension
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        HStoreExtension(),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.SlugField(blank=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(max_length=500)),
                ('is_published', models.BooleanField(default=False)),
                ('content', models.TextField(blank=True)),
                ('fragments', django.contrib.postgres.fields.hstore.HStoreField(blank=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='kopytka.Page')),
            ],
        ),
        migrations.CreateModel(
            name='StyleSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField()),
                ('description', models.CharField(blank=True, max_length=500)),
                ('source', models.TextField(blank=True)),
                ('output', models.TextField(blank=True, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, unique=True)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('content', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kopytka.Template'),
        ),
        migrations.AlterUniqueTogether(
            name='page',
            unique_together=set([('parent', 'path')]),
        ),
    ]
