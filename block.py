from hashlib import sha256
from time import time


class Block:
    """Class representing a block in the chain"""

    def __init__(self, data, prev_hash, time_stamp):
        # Number generated during mining that causes hash to be valid (proof of work)
        self.nonce = 0
        # Data that is being added in this block
        self.data = data
        # Hash of the previous block
        self.prev_hash = prev_hash
        # Time of the creation of the block
        self.time_stamp = time_stamp
        # The hash of this block overall (re-calculated during mining based on updating nonce)
        self.hash = self.block_hash()

    def block_hash(self):
        """Function that actually hashes block's data"""
        data = self.prev_hash + str(self.time_stamp) + \
            str(self.nonce) + self.data
        hashed = sha256(data.encode())
        return hashed.hexdigest()

    def mine(self, prefix_length):
        """Function that mines for a good nonce"""
        print("mining...")
        prefix_string = '0' * prefix_length
        while self.hash[0:prefix_length] != prefix_string:
            self.nonce += 1
            self.hash = self.block_hash()
        print(f"nonce found! {self.nonce}")
        return self.hash

    def __repr__(self):
        return f"<Hash><{self.hash}>\n<Data><{self.data}>"


if __name__ == '__main__':
    # The block chain
    chain = []
    # 5 isn't a great prefix length, but this is an experiment
    prefix_length = 5
    prefix_str = '0' * prefix_length

    # Function to add a new block to the chain
    def new_block(data):
        if len(chain) > 0:
            # Creating a new block
            b = Block(data, chain[-1].hash, time())
        else:
            # First block in the chain
            b = Block(data, "", time())
        # Mining step - find a hash with a set number of 0s in the prefix
        b.mine(prefix_length)
        # Add the valid block to the chain
        chain.append(b)

    new_block("hi")
    new_block("does this work?")
    new_block("testing testing")

    print("\nBLOCK CHAIN")
    for block in chain:
        print(block)
