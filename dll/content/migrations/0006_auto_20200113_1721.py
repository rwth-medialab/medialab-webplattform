# Generated by Django 2.2.9 on 2020-01-13 16:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django_extensions.db.fields
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20200113_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=datetime.datetime(2020, 1, 13, 16, 21, 3, 238862, tzinfo=utc), verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='content',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL, verbose_name='Anzeigebild'),
        ),
        migrations.AlterField(
            model_name='contentlink',
            name='type',
            field=models.CharField(choices=[('video', 'Video'), ('literature', 'Text')], max_length=10),
        ),
    ]
