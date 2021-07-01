import json
import requests
from datetime import datetime
from typing import List


class Transaction:

    def __init__(self, transaction_data: json) -> None:
        """
        Given a transaction json object, create a class that neatly contains
        all relevant information and functionality.

        Args:
            transaction_data (json) : A json response object
        """

        self.hash: str = str(transaction_data['hash'])
        self.ver: int = transaction_data['ver']
        self.vin_sz: int = transaction_data['vin_sz']
        self.vout_sz: int = transaction_data['vout_sz']
        self.size: int = transaction_data['size']
        self.weight: int = transaction_data['weight']
        self.fee: int = transaction_data['fee']
        self.relayed_by: str = transaction_data['relayed_by']
        self.lock_time: int = transaction_data['lock_time']
        self.tx_index: int = transaction_data['tx_index']
        self.double_spend: bool = transaction_data['double_spend']
        self.time: int = transaction_data['time']
        self.block_index: int = transaction_data['block_index']
        self.block_height: int = transaction_data['block_height']
        self.input_raw: List[dict] = transaction_data['inputs']
        self.output_raw: List[dict] = transaction_data['out']
        self.value: int = self.output_raw[0]['value']

        try:
            self.sender = self.input_raw[0]['prev_out']['addr']
        except Exception:
            self.sender = "Coinbase"

        self.receiver = self.output_raw[0]['addr']

    def __str__(self) -> str:
        return f"Transaction: {self.block_height}, From: {self.sender} To: {self.receiver}"

    def __repr__(self) -> str:
        return f"Repr Transaction: {self.hash}"


class Block:

    def __init__(self, block_height: int) -> None:
        """
        Given a block height, create a class instance that has all the relevant
        information that a json response from blockchain.info can gather.

        Args:
            block_height (int): The height of the block.
        """
        r = requests.get(f"https://blockchain.info/rawblock/{block_height}").json()  # nopep8
        self.hash: str = r['hash']
        self.ver: str = r['ver']
        self.prev_block: str = r['prev_block']
        self.mrkl_root: str = r['mrkl_root']
        self.timestamp: int = int(r['time'])
        self.time: datetime.datetime = datetime.fromtimestamp(self.timestamp)
        self.bits: int = r['bits']
        self.fee: int = r['fee']
        self.nonce: int = r['nonce']
        self.n_tx: int = r['n_tx']
        self.size: int = r['size']
        self.block_index: int = r['block_index']
        self.main_chain: bool = r['main_chain']
        self.height: int = r['height']
        self.weight: int = r['weight']
        self.next_block: str = r['next_block']
        self.transactions_raw: List[str] = r['tx']

        self.create_transactions(self.transactions_raw)

    def create_transactions(self, transactions) -> List[Transaction]:
        """
        Generate a list of transaction objects.

        Args:
            transactions (List[Transaction]): A list of transaction objects.
        """

        self.transactions = []

        for tx in transactions:
            self.transactions.append(Transaction(tx))


block = Block(170)
for transaction in block.transactions:
    print(transaction)
