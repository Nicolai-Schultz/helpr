# Generated by Django 5.0.2 on 2024-04-18 11:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0021_link_favorit_link"),
    ]

    operations = [
        migrations.RenameField(
            model_name="link",
            old_name="link_1",
            new_name="link",
        ),
        migrations.RemoveField(
            model_name="link",
            name="link_2",
        ),
        migrations.RemoveField(
            model_name="link",
            name="link_3",
        ),
    ]
