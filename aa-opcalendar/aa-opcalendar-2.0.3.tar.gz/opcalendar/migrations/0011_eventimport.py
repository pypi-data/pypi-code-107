# Generated by Django 3.1.2 on 2021-01-08 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("opcalendar", "0010_auto_20201105_1602"),
    ]

    operations = [
        migrations.CreateModel(
            name="EventImport",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "source",
                    models.CharField(
                        choices=[("Spectre Fleet", "Spectre Fleet")], max_length=32
                    ),
                ),
                (
                    "host",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="opcalendar.eventhost",
                    ),
                ),
                (
                    "operation_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="opcalendar.eventcategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Event Import",
                "verbose_name_plural": "Event Imports",
            },
        ),
    ]
