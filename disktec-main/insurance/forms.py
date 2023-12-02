from django import forms
from insurance.models import InsuranceClient


class InsuranceForm(forms.ModelForm):
    name = forms.CharField(
        label="Nome",
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Nome completo"}),
    )
    phone = forms.CharField(
        label="Telefone",
        required=False,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Telefone"}),
    )
    date = forms.DateField(
        label="Data do contrato",
        required=False,
        widget=forms.widgets.DateInput(
            attrs={
                "placeholder": "Data do contrato",
                "type": "text",
                "onfocus": "(this.type='date')",
                "onblur": "(this.type='text')",
            }
        ),
    )
    birth_date = forms.DateField(
        label="Data de nascimento",
        required=True,
        widget=forms.widgets.DateInput(
            attrs={
                "placeholder": "Data de nascimento",
                "type": "text",
                "onfocus": "(this.type='date')",
                "onblur": "(this.type='text')",
            }
        ),
    )
    rg = forms.CharField(
        label="RG",
        required=False,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Digite o número de RG"}),
    )
    cpf = forms.CharField(
        label="CPF",
        required=False,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Digite o número de CPF"}),
    )
    address = forms.CharField(
        label="Endereço",
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Endereço"}),
    )
    house_number = forms.IntegerField(
        label="Número",
        required=True,
        widget=forms.widgets.NumberInput(attrs={"placeholder": "Nº"}),
    )
    district = forms.CharField(
        label="Bairro",
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Bairro"}),
    )
    city = forms.CharField(
        label="Cidade",
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Cidade"}),
    )
    complement = forms.CharField(
        label="Complemento",
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Complemento"}),
    )
    machine = forms.CharField(
        label="Máquina",
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Máquina"}),
    )
    total = forms.FloatField(
        label="Valor total",
        required=True,
        widget=forms.widgets.NumberInput(attrs={"placeholder": "Valor total"}),
    )
    installments_number = forms.IntegerField(
        label="Número de parcelas",
        required=True,
        widget=forms.widgets.NumberInput(attrs={"placeholder": "Número de parcelas"}),
    )
    indemnity = forms.FloatField(
        label="Valor da indenização",
        required=True,
        widget=forms.widgets.NumberInput(attrs={"placeholder": "Valor da indenização"}),
    )
    photo = forms.ImageField(
        label="Imagem de perfil",
        required=False,
        widget=forms.widgets.FileInput(attrs={"class": "form-control"}),
    )
    expiration_date = forms.DateField(
        label="Data de vencimento",
        required=False,
        widget=forms.widgets.DateInput(
            attrs={
                "placeholder": "Data de vencimento",
                "type": "text",
                "onfocus": "(this.type='date')",
                "onblur": "(this.type='text')",
            }
        ),
    )
    obs = forms.CharField(
        label="Observações",
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Observações"}),
    )

    class Meta:
        model = InsuranceClient
        fields = [
            "name",
            "phone",
            "date",
            "birth_date",
            "rg",
            "cpf",
            "address",
            "house_number",
            "district",
            "city",
            "complement",
            "machine",
            "total",
            "installments_number",
            "indemnity",
            "photo",
            "expiration_date",
            "obs",
        ]
