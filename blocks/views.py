from blocks.models import Block
from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import BlockForm, TransactionForm
import requests


def main_view(request):
    form = BlockForm(request.POST or None)

    context = {"form": form}

    if form.is_valid():
        block_hash: str = form.cleaned_data.get('block_hash')

        block_response = requests.get(f"https://blockchain.info/rawblock/{block_hash}")

        block_response = block_response.json()

        if not block_response:
            context['correct_hash'] = False
            return render(request, "home.html", context)

        context['block'] = block_response
        context['correct_hash'] = bool(block_response)
        context['transactions'] = block_response['tx'][0:15]

    return render(request, "home.html", context)


def transaction_view(request):

    form = TransactionForm(request.POST or None)

    context = {"form": form}

    if form.is_valid():

        transaction_hash: str = form.cleaned_data.get('transaction_hash')

        transaction_response = requests.get(f"https://blockchain.info/rawtx/{transaction_hash}")

        transaction_response = transaction_response.json()

        context['transaction'] = transaction_response
        context['correct_hash'] = bool(transaction_response)

    return render(request, "transaction.html", context)
