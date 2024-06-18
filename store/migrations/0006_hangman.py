# Generated by Django 5.0.2 on 2024-03-05 11:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0005_test_udregning_db"),
    ]

    operations = [
        migrations.CreateModel(
            name="Hangman",
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
                ("word", models.CharField(max_length=50)),
                ("guess", models.CharField(max_length=1)),
            ],
        ),
    ]