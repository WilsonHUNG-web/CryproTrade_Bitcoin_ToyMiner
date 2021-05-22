import hashlib, struct, binascii
import blockcypher
from blockcypher import get_block_hash, get_block_height
from blockcypher import get_block_overview, get_latest_block_height
import datetime 
import time


def cal_block_hash(height, nonce, flag=True):
    
    if flag:
        print('height: ', height, ' nonce: ', nonce)
    myBlock = get_block_overview(str(height))
    
    timestamp_utc= myBlock['time']
    hours_added = datetime.timedelta(hours = 8)
    timestamp_correct = timestamp_utc + hours_added
    
    unixtime = time.mktime(timestamp_correct.timetuple())
    #print(unixtime)
    
    timestamp = int(unixtime)
    version = int(myBlock['ver'])
    merkle_root = myBlock['mrkl_root']
    prev_block = myBlock['prev_block']
    bits_difficulty = int(myBlock['bits'])
    #nonce = int(myBlock['nonce'])
    
    header = ( struct.pack("<L", version) + 
                  bytes.fromhex(prev_block)[::-1] +
                  bytes.fromhex(merkle_root)[::-1] +
                  struct.pack("<LLL", timestamp, bits_difficulty, nonce))
    
    hash_result = hashlib.sha256(hashlib.sha256(header).digest()).digest()
    return bytes.hex(hash_result[::-1])


if __name__ == '__main__':
    print('===============================================================================================')
    print('Student: Weishiun HUNG, ID: 109065527')
    print('=====================================Test_paper.txt============================================\n', 
        'height = 566023: \n',
        'nonce = 0xae443126     hash =', cal_block_hash(566023, 0xae443126, False), '\n',
        'nonce = 0xae443127     hash =', cal_block_hash(566023, 0xae443127, False), '\n',
        'nonce = 0xae443128     hash = 00000000000000000025a9c24d3f7cac8a2acf9ee6fbf627cc71cd1b8942da43\n',
        '==============================================================================================\n')



    print('=============================================================================== \n')
    print('Below down you may edit the function input to test the blockhash output.\n')
    print('e.g. cal_block_hash(566023, 0xae443128) which means cal_block_hash(Height, Nonce)\n')
    print('=============================================================================== ')
    print('[Result]')
    print('hash: ',cal_block_hash(566023, 0xae443128)) ##cal_block_hash(Height, Nonce)




