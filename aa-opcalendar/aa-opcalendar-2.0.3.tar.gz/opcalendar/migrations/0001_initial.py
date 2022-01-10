# Generated by Django 3.1.2 on 2020-11-04 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("eveonline", "0012_index_additions"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="General",
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
            ],
            options={
                "permissions": (
                    ("basic_access", "Can access this app"),
                    ("view_public", "Can see public events"),
                    ("view_member", "Can see member events"),
                    ("create_event", "Can create and edit events"),
                    ("manage_event", "Can delete and manage signups"),
                ),
                "managed": False,
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="EventCategory",
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
                ("name", models.CharField(max_length=150)),
                ("ticker", models.CharField(max_length=10)),
                (
                    "color",
                    models.CharField(
                        choices=[
                            ("green", "Green"),
                            ("red", "Red"),
                            ("orange", "Orange"),
                            ("blue", "Blue"),
                            ("grey", "Grey"),
                            ("yellow", "Yellow"),
                        ],
                        default="green",
                        max_length=6,
                    ),
                ),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="WebHook",
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
                ("name", models.CharField(max_length=150)),
                ("webhook_url", models.CharField(max_length=500)),
                ("enabled", models.BooleanField()),
            ],
            options={
                "verbose_name": "Webhook",
                "verbose_name_plural": "Webhooks",
            },
        ),
        migrations.CreateModel(
            name="EventSignal",
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
                ("ignore_past_fleets", models.BooleanField(default=True)),
                (
                    "webhook",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="opcalendar.webhook",
                    ),
                ),
            ],
            options={
                "verbose_name": "Fleet Signal",
                "verbose_name_plural": "Fleet Signals",
            },
        ),
        migrations.CreateModel(
            name="Event",
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
                ("title", models.CharField(max_length=200)),
                ("doctrine", models.CharField(default="", max_length=254)),
                ("formup_system", models.CharField(default="", max_length=254)),
                ("description", models.TextField()),
                ("start_time", models.DateTimeField()),
                ("end_time", models.DateTimeField()),
                ("fc", models.CharField(default="", max_length=254)),
                (
                    "visibility",
                    models.CharField(
                        choices=[
                            ("Public", "Public access"),
                            ("Member", "Members only access"),
                        ],
                        db_index=True,
                        default="Public",
                        max_length=7,
                    ),
                ),
                (
                    "created_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "eve_character",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="eveonline.evecharacter",
                    ),
                ),
                (
                    "operation_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="opcalendar.eventcategory",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EventMember",
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
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="opcalendar.event",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("event", "user")},
            },
        ),
    ]
