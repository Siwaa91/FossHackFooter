# Generated by Django 3.1.2 on 2023-10-17 07:58

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    replaces = [('resources', '0001_initial'), ('resources', '0002_auto_20201106_0420'), ('resources', '0003_auto_20201109_0412'), ('resources', '0004_auto_20201109_1504'), ('resources', '0005_auto_20201109_1620'), ('resources', '0006_auto_20201110_1333'), ('resources', '0007_auto_20201110_1434'), ('resources', '0008_auto_20201110_1439'), ('resources', '0009_auto_20201110_1441'), ('resources', '0010_auto_20201110_1444'), ('resources', '0011_auto_20201110_1447'), ('resources', '0012_auto_20201110_2049'), ('resources', '0013_auto_20201110_2049'), ('resources', '0014_auto_20201110_2053'), ('resources', '0015_auto_20210111_1357'), ('resources', '0016_auto_20210111_1359')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Litigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.TextField()),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(default='Write your blog here!')),
                ('url', models.URLField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('published_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='PolicyTracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.TextField()),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(default='Write your blog here!')),
                ('url', models.URLField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('published_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='RelevantResearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.TextField()),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(default='Write your blog here!')),
                ('url', models.URLField()),
                ('published_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RtiAndOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.TextField()),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(default='Write your blog here!')),
                ('url', models.URLField()),
                ('published_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Conferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.TextField()),
                ('url', models.URLField()),
                ('published_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(default='Write your blog here!')),
            ],
        ),
    ]