# Generated by Django 5.0.6 on 2024-06-11 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("community", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="communityfollowers",
            name="accepted",
            field=models.BooleanField(default=True),
        ),
    ]