# Generated by Django 4.0.6 on 2022-07-13 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("insurance", "0002_insuranceclient_paid"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="insuranceclient",
            name="paid",
        ),
        migrations.AddField(
            model_name="insuranceclient",
            name="last_payment",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="insuranceclient",
            name="payment_status",
            field=models.CharField(default="pago", max_length=255),
        ),
    ]
