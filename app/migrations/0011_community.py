# Generated by Django 5.0.6 on 2024-06-09 13:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0010_thread_published_at_thread_status_thread_updated"),
        ("users", "0009_moderators"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Community",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(max_length=500)),
                ("is_private", models.BooleanField(default=False)),
                (
                    "admins",
                    models.ManyToManyField(related_name="admins", to="users.moderators"),
                ),
                (
                    "followers",
                    models.ManyToManyField(related_name="community_followers", to=settings.AUTH_USER_MODEL),
                ),
                (
                    "posts",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="posts",
                        to="users.publication",
                    ),
                ),
                (
                    "users",
                    models.ManyToManyField(related_name="users", to=settings.AUTH_USER_MODEL),
                ),
            ],
        ),
    ]