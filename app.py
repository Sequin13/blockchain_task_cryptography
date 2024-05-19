from flask import Flask, render_template, request, jsonify
from blockchain import Blockchain
from blockNode import Node

app = Flask(__name__)
blockchain = Blockchain()
node = Node()

@app.route('/')
def index():
    """
    Render the index page with wallet information.

    Returns:
        HTML: Rendered template containing wallet information.
    """
    wallet = node.wallet
    return render_template('index.html', wallet=wallet)

@app.route('/transaction', methods=['GET', 'POST'])
def transaction():
    """
    Handle transaction requests.

    If the request method is POST, processes the transaction and updates the balance.
    If the request method is GET, renders the transaction page with wallet information.

    Returns:
        str or HTML: If POST request, a message indicating transaction submission and updated balance.
                     If GET request, rendered template containing wallet information.
    """
    if request.method == 'POST':
        sender = request.form['sender']
        recipient = request.form['recipient']
        amount = float(request.form['amount'])
        node.send_transaction(sender, recipient, amount)
        balance = node.get_balance(sender)
        return f'Transaction submitted \n Your balance is now: {balance}'
    wallet = node.wallet
    wallet2 = node.wallet2
    return render_template('transaction.html', wallet=wallet, wallet2=wallet2)

@app.route('/wallets', methods=['POST'])
def create_wallet():
    """
    Create a new wallet.

    Returns:
        JSON: New wallet address.
    """
    wallet = node.create_wallet()
    return jsonify({'address': wallet.address}), 200

@app.route('/balance/<address>', methods=['GET'])
def get_balance(address):
    """
    Get the balance of a wallet address.

    Args:
        address (str): Wallet address to retrieve balance for.

    Returns:
        JSON: Wallet balance.
    """
    balance = node.get_balance(address)
    return jsonify({'balance': balance}), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """
    Add a new transaction to the blockchain.

    Returns:
        JSON: Confirmation message.
    """
    values = request.get_json()
    required_fields = ['sender', 'recipient', 'amount']
    if not all(field in values for field in required_fields):
        return 'Missing fields', 400
    node.send_transaction(values['sender'], values['recipient'], values['amount'])
    return jsonify({'message': 'Transaction will be added to the blockchain'}), 201

@app.route('/chain', methods=['GET'])
def get_chain():
    """
    Get the current blockchain.

    Returns:
        JSON: Current blockchain.
    """
    chain = blockchain.chain
    return jsonify({'chain': chain}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
