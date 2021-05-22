# CryproTrade_Bitcoin

--How to run

The first part, Nonce_verifier.py, is a simple code which can generate a block hash with provided block height and nonce to verify the correctness of the nonce.
And the second part, Virtual_Mining.py, also provides a mining method to mine BTC according to the lastest block info online.

1.	Firstly install the blockcypher package by the command:
```
$ pip3 install blockcypher
```
2.	To verify the nonce, run Nonce_verifier.py by the command:
```
$ python 109065527_MidTerm_Project_Nonce_verifier.py
```
Ps.
If you want to specify the Height and Nonce, go to the bottom line in this *.py file and edit the function input of cal_block_hash(Height, Nonce) as shown below.

3.	To start mining, run the Virtual_Mining.py by the command:
```
$ python 109065527_MidTerm_Project_Mining.py
```
