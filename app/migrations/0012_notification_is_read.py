# Generated by Django 5.0.6 on 2024-06-13 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0011_notification"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="is_read",
            field=models.BooleanField(default=False),
        ),
    ]
