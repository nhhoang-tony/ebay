# Generated by Django 3.1.7 on 2021-04-18 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_listings_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bids',
            name='bid',
            field=models.DecimalField(decimal_places=2, max_digits=19),
        ),
        migrations.AlterField(
            model_name='listings',
            name='bid',
            field=models.DecimalField(decimal_places=2, max_digits=19),
        ),
    ]