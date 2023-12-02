import datetime
from dateutil.relativedelta import relativedelta
from django.shortcuts import redirect, render
from insurance.forms import InsuranceForm
from rent.forms import RentForm
from sale.forms import SaleForm
from service.forms import ServiceForm
from insurance.models import InsuranceClient
from rent.models import RentClient
from sale.models import SaleClient
from service.models import ServiceClient
from controller.functions import update_payment_status, machine_count


def home(request):
    return render(request, "home.html")


def insurance(request):
    show_form = True
    show_search = True

    clients = InsuranceClient.objects.all()
    machines_count = machine_count(InsuranceClient)
    update_payment_status(clients)

    query = request.GET.get("search_bar")
    if query != "" and query is not None:
        q1 = clients.filter(name__icontains=query)
        q2 = clients.filter(cpf__icontains=query)
        q3 = clients.filter(rg__icontains=query)
        clients = q1.union(q2, q3)

        show_form = False

    if request.method == "POST":
        form = InsuranceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = InsuranceForm()
    else:
        form = InsuranceForm()

    context = {
        "form": form,
        "clients": clients,
        "machines_count": machines_count,
        "show_form": show_form,
        "show_search": show_search,
    }
    return render(request, "insurance.html", context)


def rent(request):
    show_form = True
    show_search = True

    clients = RentClient.objects.all()
    machines_count = machine_count(RentClient)
    update_payment_status(clients)

    query = request.GET.get("search_bar")
    if query != "" and query is not None:
        q1 = clients.filter(name__icontains=query)
        q2 = clients.filter(cpf__icontains=query)
        q3 = clients.filter(rg__icontains=query)
        clients = q1.union(q2, q3)

        show_form = False

    if request.method == "POST":
        form = RentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = RentForm()
    else:
        form = RentForm()

    context = {
        "form": form,
        "clients": clients,
        "machines_count": machines_count,
        "show_form": show_form,
        "show_search": show_search,
    }
    return render(request, "rent.html", context)


def sale(request):
    show_form = True
    show_search = True

    clients = SaleClient.objects.all()
    query = request.GET.get("search_bar")
    if query != "" and query is not None:
        q1 = clients.filter(name__icontains=query)
        q2 = clients.filter(cpf__icontains=query)
        q3 = clients.filter(rg__icontains=query)
        clients = q1.union(q2, q3)

        show_form = False

    if request.method == "POST":
        form = SaleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = SaleForm()
    else:
        form = SaleForm()

    context = {
        "form": form,
        "clients": clients,
        "show_form": show_form,
        "show_search": show_search,
    }
    return render(request, "sale.html", context)


def service(request):
    show_form = True
    show_search = True

    clients = ServiceClient.objects.all()
    query = request.GET.get("search_bar")
    if query != "" and query is not None:
        q1 = clients.filter(name__icontains=query)
        q2 = clients.filter(cpf__icontains=query)
        q3 = clients.filter(rg__icontains=query)
        clients = q1.union(q2, q3)

        show_form = False

    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ServiceForm()
    else:
        form = ServiceForm()

    context = {
        "form": form,
        "clients": clients,
        "show_form": show_form,
        "show_search": show_search,
    }
    return render(request, "service.html", context)


def pay(request, contract, pk):
    if contract == "insurance":
        client = InsuranceClient.objects.get(pk=pk)
        client.last_payment = datetime.date.today()
        client.expiration_date += relativedelta(months=1)
        client.payment_status = 4  # pago
        client.save()
        return redirect(insurance)

    elif contract == "rent":
        client = RentClient.objects.get(pk=pk)
        client.last_payment = datetime.date.today()
        client.expiration_date += relativedelta(months=1)
        client.payment_status = 4  # pago
        client.save()
        return redirect(rent)


def edit(request, contract, pk):
    show_form = True
    show_search = False
    clients = {}

    if contract == "insurance":
        client = InsuranceClient.objects.get(id=pk)
        if request.method == "POST":
            form = InsuranceForm(request.POST, request.FILES, instance=client)
            if form.is_valid():
                form.save()
                return redirect(insurance)
        else:
            form = InsuranceForm(instance=client)
        context = {
            "form": form,
            "clients": clients,
            "show_form": show_form,
            "show_search": show_search,
        }
        return render(request, "insurance.html", context)

    elif contract == "rent":
        client = RentClient.objects.get(id=pk)
        if request.method == "POST":
            form = RentForm(request.POST, request.FILES, instance=client)
            if form.is_valid():
                form.save()
                return redirect(rent)
        else:
            form = RentForm(instance=client)
        context = {
            "form": form,
            "clients": clients,
            "show_form": show_form,
            "show_search": show_search,
        }
        return render(request, "rent.html", context)

    elif contract == "sale":
        client = SaleClient.objects.get(id=pk)
        if request.method == "POST":
            form = SaleForm(request.POST, request.FILES, instance=client)
            if form.is_valid():
                form.save()
                return redirect(sale)
        else:
            form = SaleForm(instance=client)
        context = {
            "form": form,
            "clients": clients,
            "show_form": show_form,
            "show_search": show_search,
        }
        return render(request, "sale.html", context)

    elif contract == "service":
        client = ServiceClient.objects.get(id=pk)
        if request.method == "POST":
            form = ServiceForm(request.POST, request.FILES, instance=client)
            if form.is_valid():
                form.save()
                return redirect(service)
        else:
            form = ServiceForm(instance=client)
        context = {
            "form": form,
            "clients": clients,
            "show_form": show_form,
            "show_search": show_search,
        }
        return render(request, "service.html", context)


def delete(request, contract, pk):
    if contract == "insurance":
        client = InsuranceClient.objects.get(id=pk)
        client.delete()
        return redirect(insurance)

    elif contract == "rent":
        client = RentClient.objects.get(id=pk)
        client.delete()
        return redirect(rent)

    elif contract == "sale":
        client = SaleClient.objects.get(id=pk)
        client.delete()
        return redirect(sale)

    elif contract == "service":
        client = ServiceClient.objects.get(id=pk)
        client.delete()
        return redirect(service)


def print(request, contract, pk):
    if contract == "insurance":
        return render(request, "insurance_contract.html")
    elif contract == "rent":
        return render(request, "rent_contract.html")
