# Generated by Django 5.0.6 on 2024-06-09 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0014_alter_community_followers"),
        ("users", "0009_moderators"),
    ]

    operations = [
        migrations.AlterField(
            model_name="community",
            name="posts",
            field=models.ManyToManyField(related_name="posts", to="users.publication"),
        ),
    ]
