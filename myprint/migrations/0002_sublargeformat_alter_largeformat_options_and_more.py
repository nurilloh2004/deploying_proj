# Generated by Django 4.1.2 on 2022-10-27 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("myprint", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SubLargeFormat",
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
                ("product_name", models.CharField(max_length=50)),
                ("type", models.CharField(max_length=50)),
                ("price", models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name="largeformat",
            options={},
        ),
        migrations.RemoveField(
            model_name="largeformat",
            name="price",
        ),
        migrations.RemoveField(
            model_name="largeformat",
            name="price1",
        ),
        migrations.RemoveField(
            model_name="largeformat",
            name="price2",
        ),
        migrations.RemoveField(
            model_name="largeformat",
            name="price3",
        ),
        migrations.RemoveField(
            model_name="largeformat",
            name="price4",
        ),
        migrations.RemoveField(
            model_name="largeformat",
            name="product_name",
        ),
        migrations.RemoveField(
            model_name="largeformat",
            name="product_name1",
        ),
        migrations.RemoveField(
            model_name="largeformat",
            name="product_name2",
        ),
        migrations.RemoveField(
            model_name="largeformat",
            name="product_name4",
        ),
        migrations.RemoveField(
            model_name="largeformat",
            name="type",
        ),
        migrations.RemoveField(
            model_name="largeformat",
            name="type1",
        ),
        migrations.RemoveField(
            model_name="largeformat",
            name="type2",
        ),
        migrations.RemoveField(
            model_name="largeformat",
            name="type3",
        ),
        migrations.RemoveField(
            model_name="largeformat",
            name="type4",
        ),
        migrations.DeleteModel(
            name="Type_Services",
        ),
        migrations.AddField(
            model_name="sublargeformat",
            name="all",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="myprint.largeformat"
            ),
        ),
    ]
