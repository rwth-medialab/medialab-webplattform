# Generated by Django 2.2.14 on 2020-07-28 12:58

from django.db import migrations, models
import django_extensions.db.fields
import dll.content.models


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0011_auto_20200714_1708"),
    ]

    operations = [
        migrations.AddField(
            model_name="teachingmodule",
            name="hybrid",
            field=models.BooleanField(
                default=False, verbose_name="Geeignet für Hybridunterricht"
            ),
        ),
        migrations.AlterField(
            model_name="content",
            name="created",
            field=django_extensions.db.fields.CreationDateTimeField(
                auto_now_add=True,
                default=dll.content.models.get_default_created_time,
                null=True,
                verbose_name="created",
            ),
        ),
    ]