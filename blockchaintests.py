import unittest
from blockNode import Wallet, Wallet2, Node
from blockchain import Blockchain


class TestWallet(unittest.TestCase):
    def test_wallet_attributes(self):
        wallet = Wallet()
        self.assertTrue(hasattr(wallet, 'address'))
        self.assertTrue(hasattr(wallet, 'balance'))
        self.assertIsInstance(wallet.address, str)
        self.assertIsInstance(wallet.balance, float)

    def test_wallet2_attributes(self):
        wallet2 = Wallet2()
        self.assertTrue(hasattr(wallet2, 'address'))
        self.assertTrue(hasattr(wallet2, 'balance'))
        self.assertIsInstance(wallet2.address, str)
        self.assertIsInstance(wallet2.balance, float)

    def test_node_attributes(self):
        node = Node()
        self.assertTrue(hasattr(node, 'blockchain'))
        self.assertTrue(hasattr(node, 'wallet'))
        self.assertTrue(hasattr(node, 'wallet2'))
        self.assertIsInstance(node.blockchain, Blockchain)
        self.assertIsInstance(node.wallet, Wallet)
        self.assertIsInstance(node.wallet2, Wallet2)

    def test_create_wallet(self):
        node = Node()
        new_wallet = node.create_wallet()
        self.assertIsInstance(new_wallet, Wallet)


class TestBlockchain(unittest.TestCase):
    def test_blockchain_attributes(self):
        blockchain = Blockchain()
        self.assertTrue(hasattr(blockchain, 'chain'))
        self.assertTrue(hasattr(blockchain, 'current_transactions'))
        self.assertIsInstance(blockchain.chain, list)
        self.assertIsInstance(blockchain.current_transactions, list)

    def test_new_block(self):
        blockchain = Blockchain()
        proof = 123
        previous_hash = 'previous_hash'
        block = blockchain.new_block(proof, previous_hash)
        self.assertIsInstance(block, dict)
        self.assertIn('index', block)
        self.assertIn('timestamp', block)
        self.assertIn('transactions', block)
        self.assertIn('proof', block)
        self.assertIn('previous_hash', block)
        self.assertEqual(block['proof'], proof)
        self.assertEqual(block['previous_hash'], previous_hash)

    def test_new_transaction(self):
        blockchain = Blockchain()
        sender = 'sender_address'
        recipient = 'recipient_address'
        amount = 123.45
        index = blockchain.new_transaction(sender, recipient, amount)
        self.assertIsInstance(index, int)
        self.assertEqual(index, blockchain.last_block['index'] + 1)



if __name__ == '__main__':
    unittest.main()
