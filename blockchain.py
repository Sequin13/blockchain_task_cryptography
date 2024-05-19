import hashlib
import json
from time import time

class Blockchain:
    """
    A class representing a blockchain.

    Attributes:
        chain (list): A list of blocks forming the blockchain.
        current_transactions (list): A list of pending transactions.
    """
    def __init__(self):
        """
        Initialize a new Blockchain instance.

        Initializes the blockchain with a genesis block.
        """
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Create a new block in the blockchain.

        Args:
            proof (int): The proof of work for the new block.
            previous_hash (str): The hash of the previous block.

        Returns:
            dict: The newly created block.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Add a new transaction to the list of pending transactions.

        Args:
            sender (str): The address of the sender.
            recipient (str): The address of the recipient.
            amount (float): The amount to be transferred.

        Returns:
            int: The index of the block that will hold this transaction.
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    @property
    def last_block(self):
        """
        Get the last block in the blockchain.

        Returns:
            dict: The last block in the blockchain.
        """
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        Generate the SHA-256 hash of a block.

        Args:
            block (dict): The block to be hashed.

        Returns:
            str: The SHA-256 hash of the block.
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
