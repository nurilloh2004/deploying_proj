# Generated by Django 4.1.1 on 2022-10-11 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprint', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderform',
            name='VAT',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderform',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderform',
            name='name',
            field=models.CharField(blank=True, max_length=65, null=True),
        ),
        migrations.AlterField(
            model_name='orderform',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderform',
            name='price_free_VAT',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderform',
            name='price_with_VAT',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderform',
            name='total',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderform',
            name='total_price_ALL',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderform',
            name='total_price_with_VAT',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
