# Generated by Django 4.1.2 on 2022-10-25 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myprint", "0003_alter_sponsors_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="HomeDescription",
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
                ("description", models.TextField()),
            ],
        ),
    ]
