import uuid
from blockchain import Blockchain

class Wallet:
    """
    A class representing a wallet (sender) with a unique address and balance.
    For simulation purposes only

    Attributes:
        address (str): A unique identifier for the wallet.
        balance (float): The current balance in the wallet.
    """
    def __init__(self):
        """
        Initialize a new Wallet instance.

        Sets a unique UUID as the address and an initial balance of 10000.
        """
        self.address = str(uuid.uuid4())
        self.balance = 10000.0

class Wallet2:
    """
    A class representing a second wallet (reciever) for simulation purposes only.

    Attributes:
        address (str): A fixed address for the wallet.
        balance (float): The current balance in the wallet.
    """
    def __init__(self):
        """
        Initialize a new Wallet2 instance.

        Sets a fixed address and an initial balance of 10000.
        """
        self.address = "0d6ed5ab-ff80-46cd-b064-5cc15c4c5cb7"
        self.balance = 10000.0

class Node:
    """
    A class representing a node in the blockchain network.

    Attributes:
        blockchain (Blockchain): The blockchain instance associated with the node.
        wallet (Wallet): The primary wallet instance associated with the node.
        wallet2 (Wallet2): A secondary wallet instance for simulation purposes.
    """
    def __init__(self):
        """
        Initialize a new Node instance.

        Creates a new blockchain, a primary wallet, and a secondary wallet.
        """
        self.blockchain = Blockchain()
        self.wallet = Wallet()
        self.wallet2 = Wallet2()

    def create_wallet(self):
        """
        Create a new wallet.

        Returns:
            Wallet: A new instance of the Wallet class.
        """
        return Wallet()

    def get_balance(self, address):
        """
        Get the balance of a wallet.

        Args:
            address (str): The address of the wallet to retrieve the balance for.

        Returns:
            float or str: The balance of the wallet if found, or a message indicating address not found.
        """
        if address == self.wallet.address:
            return self.wallet.balance
        return 'Address not found'

    def send_transaction(self, sender, recipient, amount):
        """
        Send a transaction from one wallet to another.

        Args:
            sender (str): The address of the sender wallet.
            recipient (str): The address of the recipient wallet.
            amount (float): The amount to be sent in the transaction.

        Returns:
            str: A message indicating the transaction status.
        """
        if sender == self.wallet.address:
            if self.wallet.balance >= amount:
                self.wallet.balance -= amount
                self.blockchain.new_transaction(sender, recipient, amount)
                return 'Transaction successful'
            else:
                return 'Insufficient funds'
        return 'Invalid sender address'
