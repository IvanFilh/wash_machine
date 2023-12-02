from django.db import models


class SaleClient(models.Model):
    name = models.CharField(max_length=255, unique=False, null=False)
    phone = models.CharField(max_length=255, null=True)
    date = models.DateField(null=True)
    birth_date = models.DateField(null=False)
    rg = models.CharField(max_length=255, unique=True, null=True)
    cpf = models.CharField(max_length=255, unique=True, null=True)
    address = models.CharField(max_length=255, unique=False, null=False)
    house_number = models.IntegerField(unique=False, null=True)
    district = models.CharField(max_length=255, unique=False, null=False)
    city = models.CharField(max_length=255, unique=False, null=False)
    complement = models.CharField(max_length=255, unique=False, null=False)
    photo = models.ImageField(upload_to="media", null=True)
    machine = models.CharField(max_length=255, unique=False, null=True)
    installments_value = models.FloatField(max_length=255, unique=False, null=False)
    total = models.FloatField(max_length=255, unique=False, null=False)
    payment = models.CharField(max_length=255, unique=False, null=False)
    obs = models.CharField(max_length=255, unique=False, null=True)

    class Meta:
        ordering = ("machine",)
