# Generated by Django 4.0.6 on 2022-07-07 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ServiceClient",
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
                ("name", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=255, null=True)),
                ("date", models.DateField(null=True)),
                ("birth_date", models.DateField()),
                ("rg", models.CharField(max_length=255, null=True, unique=True)),
                ("cpf", models.CharField(max_length=255, null=True, unique=True)),
                ("address", models.CharField(max_length=255)),
                ("house_number", models.IntegerField(null=True)),
                ("district", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=255)),
                ("complement", models.CharField(max_length=255)),
                ("photo", models.ImageField(null=True, upload_to="media")),
                ("service_type", models.CharField(max_length=255)),
                ("machine", models.CharField(max_length=255, null=True)),
                ("total", models.FloatField(max_length=255)),
                ("payment", models.CharField(max_length=255)),
                ("obs", models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
