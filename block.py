from time import time

from utility.printable import Printable

# adding a block class to make code more readable 
class Block(Printable):
    def __init__(self, index, previous_hash, transactions, proof, time=time()):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time
        self.transactions = transactions
        self.proof = proof