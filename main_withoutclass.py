import numpy as np
from hashlib import sha256
from time import time
import pdb

difficulty = 4
blockchain = []

prev_hash = 'Genesis'

data = {
    'name' : 'name',
    'usage' : 'usage',
    'amount' : 'amount',
    }

nonce = 0
datastr = data['name']+data['usage']+data['amount']+prev_hash+str(nonce)
cur_hash = sha256(datastr.encode()).hexdigest()

# print(datastr)
# print(nonce, cur_hash)

nonce_check = '0'*difficulty

while not cur_hash.startswith(nonce_check): # while new_hash[:difficulty] != nonce_check:
    nonce += 1 
    datastr = data['name']+data['usage']+data['amount']+prev_hash+str(nonce)
    cur_hash = sha256(datastr.encode()).hexdigest()

# print(datastr)
# print(nonce, cur_hash)
# pdb.set_trace()

block = (data, prev_hash, cur_hash, nonce)
blockchain.append(block)

pdb.set_trace()
# 'prev_hash' : prev_hash,
# 'cur_hash' : cur_hash,
