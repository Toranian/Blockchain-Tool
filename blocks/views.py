from blocks.models import Block
from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import BlockForm, TransactionForm
import requests
# from .utils import Block
from .utils import Block, Transaction

def main_view(request):
    form = BlockForm(request.POST or None)

    context = {"form": form}

    if form.is_valid():
        # block_hash: str = form.cleaned_data.get('block_hash')

        # block_response = requests.get(f"https://blockchain.info/rawblock/{block_hash}")

        # block_response = block_response.json()

        # if not block_response:
        #     context['correct_hash'] = False
        #     return render(request, "home.html", context)

        block = Block(form.cleaned_data.get('block_hash')) 

        context['block'] = block
        # context['sender'] = block.transaction.sender
        # context['receiver'] = block.transaction.receiver
        context['time'] = block.time
        
        # context['correct_hash'] = 
        context['transactions'] = block.transactions

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
