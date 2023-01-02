# Generated by Django 4.1.3 on 2022-12-18 11:19

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_articles_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', unique=True),
        ),
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', unique=True),
        ),
    ]
