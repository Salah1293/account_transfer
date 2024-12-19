from django.shortcuts import render, redirect
from .forms import *
from .models import *
import csv
from django.contrib import messages
from .utils import *
from django.db import transaction


# Create your views here.

#import csv file of accounts view
def import_accounts(request):
    form = None
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.cleaned_data['document']

            if not document.name.endswith('.csv'):
                messages.error(request, 'only csv files are supported.')
                return redirect('import_accounts')
            

            try:
                uploaded_file = document.read().decode('utf-8').splitlines()
                reader = csv.reader(uploaded_file)
                headers = next(reader)
                for row in reader:
                    id, name, balance = row
                    Account.objects.update_or_create(id=id, defaults={'balance': balance, 'name': name})

            except Exception as e:
                messages.error(request, f'error importing accounts {e}')
            return redirect('list_accounts')
    else:
        form = UploadForm()

    context = {'form': form}
    return render(request, 'account/import_accounts.html', context)


#list accounts details view
def list_accounts(request):
    accounts = Account.objects.all()
    custom_range, paginated_accounts = paginate(request, accounts)
    context = {'accounts': paginated_accounts, 'custom_range': custom_range}
    return render(request, 'account/list_accounts.html', context)


#transfer between acounts view
def transfer_funds(request):
    if request.method == 'POST':
        form = TransferFundsForm(request.POST)
        if form.is_valid():
            source_account = form.cleaned_data['source_account']
            target_account = form.cleaned_data['target_account']
            amount = form.cleaned_data['amount']

            if source_account.balance < amount:
                messages.error(request, "Insufficient funds in the source account.")
            else:
                try:
                    with transaction.atomic(): 
                        source_account.balance -= amount
                        source_account.save()

                        target_account.balance += amount
                        target_account.save()

                    return redirect('list_accounts')
                except Exception as e:
                    messages.error(request, f"An error occurred: {str(e)}")
        else:
            messages.error(request, "Invalid input. Please provide a valid amount.")
    else:
        form = TransferFundsForm()

    context = {'form': form}
    return render(request, 'account/transfer_funds.html', context)