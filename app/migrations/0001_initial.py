# Generated by Django 5.0.6 on 2024-05-21 14:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Thread",
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
                ("title", models.CharField(max_length=255)),
                ("context", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("image", models.ImageField(blank=True, upload_to="images/")),
                ("file", models.FileField(blank=True, upload_to="files/")),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="threads",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
