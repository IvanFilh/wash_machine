# Generated by Django 4.0.6 on 2022-07-13 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rent", "0003_remove_rentclient_paid_rentclient_last_payment_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rentclient",
            name="payment_status",
            field=models.IntegerField(default=3),
        ),
    ]
