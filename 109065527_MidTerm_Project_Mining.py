#!/usr/bin/env python
# coding: utf-8

# In[1]:


import hashlib, struct, binascii
import blockcypher
from blockcypher import get_block_hash, get_block_height
from blockcypher import get_block_overview, get_latest_block_height
import datetime 
import time

def hash_256(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()

class Block:
    def __init__(self):
        self.transactions = []
        self.hash_merkle_block = None
        self.nonce = 0

    def add_new_transaction(self, new_transaction):
        if not self.is_block_full():
            self.transactions.append(new_transaction)
            self.hash_merkle_block = hash_256(str(''.join(self.transactions)))
            return False
        else:
            return True

    def is_block_full(self):
        # We assume a block can contain 1000 transactions at most.
        return len(self.transactions) >= 1000
    
class TransactionSource:
    def __init__(self):
        self.iseed = 0

    def generate_transaction(self):
        transaction_payload = 'This is a new transaction record:{}'.format(self.iseed)
        transaction_hash = hash_256(transaction_payload)
        self.iseed += 1
        return transaction_hash


# In[2]:


from hashlib import sha256
from blockcypher import get_latest_block_hash

def cal_target(bits):
    exp = bits >> 24
    mant = bits & 0xffffff
    target_hexstr = '%064x' % (mant * (1<<(8*(exp - 3))))
    print(f'Target: {target_hexstr}')
    return target_hexstr

def SHA256(text):
    return hashlib.sha256(text.encode("ascii")).hexdigest()

def mine(timestamp,version, merkle_root, prev_block, bits_difficulty ,prefix_zeros):
    prefix_zeros = '0'*prefix_zeros
    found_solution =False
    nonce = 0
    while not (found_solution):
        header = ( struct.pack("<L", version) +                  bytes.fromhex(prev_block)[::-1] +                  bytes.fromhex(merkle_root)[::-1] +                  struct.pack("<LLL", timestamp, bits_difficulty, nonce))
        hash_result = hashlib.sha256(hashlib.sha256(header).digest()).digest()
        hash_result_str = bytes.hex(hash_result[::-1])
        if hash_result_str.startswith(prefix_zeros):
            print(f"!!!Success, mined bitcoins with nonce value:{nonce}")
            found_solution = True
            return new_hash
        else:
            print('Failed.'' Nonce: ', nonce, ' Hash: ', hash_result_str)
            nonce = nonce + 1

def count_leading_zeros(target_hash):
    for i in range(64, 0, -1):
        zeros = ''
        for j in range(i):
            zeros = zeros + '0'
        if target_hash.startswith(zeros):
            return i
        
def get_timestamp(Block_overview):
    timestamp_utc= Block_overview['time']
    hours_added = datetime.timedelta(hours = 8)
    timestamp_correct = timestamp_utc + hours_added
    unixtime = time.mktime(timestamp_correct.timetuple())
    
    return int(unixtime)

if __name__=='__main__':
    
    
    #Declare an object to generate new transaction records to simulate the current pending transactions
    transaction_source = TransactionSource()

    New_block = Block()
    for i in range(1234): #there are 1234 pending transactions, assuming a block can contain only 1000 transactions
        new_trans = transaction_source.generate_transaction()
        if New_block.add_new_transaction(new_trans): #updates merkle tree till 1000 transactions are added then break loop
            break
        
    #get the lastest block hash by the blockcypher lib function
    lastest_block_hash = get_latest_block_hash()
    LatestBlock = get_block_overview(lastest_block_hash)
    
    ## five items to be placed in the header without nonce
    timestamp = get_timestamp(LatestBlock)
    version = int(LatestBlock['ver'])
    merkle_hash = New_block.hash_merkle_block
    prev_block = LatestBlock['prev_block']
    bits_difficulty = LatestBlock['bits']
    ##
    
    difficulty= count_leading_zeros(cal_target(LatestBlock['bits']))  #calculate how many zeros we need as prefix

    #Start mining
    start_time = time.time()
    print("=========================Start mining===========================")
    new_hash = mine(timestamp, version, merkle_hash, prev_block, bits_difficulty, difficulty)
    total_time = str((time.time() - start_time))
    print(f"====================end mining. Mining took: {total_time} seconds======================")
    print(new_hash)


# In[ ]:




