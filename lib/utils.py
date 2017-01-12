import hashlib


def get_block_hash(chain_id, block_id, data, previous_hash, nonce, created_at):
    str_tmp = str(chain_id)+str(block_id)+str(data)+previous_hash+str(nonce)+str(created_at)
    return