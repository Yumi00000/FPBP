# Generated by Django 5.0.6 on 2024-06-09 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0011_community"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="community",
            name="users",
        ),
    ]
