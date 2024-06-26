# Generated by Django 5.0.2 on 2024-04-09 10:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0019_stats_trin_1_stats_trin_2_stats_trin_3"),
    ]

    operations = [
        migrations.AddField(
            model_name="stats",
            name="copc",
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="stats",
            name="copc_2",
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="stats",
            name="copc_3",
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="stats",
            name="csat",
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="stats",
            name="csat_2",
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="stats",
            name="csat_3",
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="stats",
            name="trin_1",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="stats",
            name="trin_2",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="stats",
            name="trin_3",
            field=models.CharField(max_length=20),
        ),
    ]
