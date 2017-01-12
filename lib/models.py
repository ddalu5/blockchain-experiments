import re
import uuid
import hashlib
from datetime import datetime
from settings import VALID_SIGNATURE


class Block:

    def __init__(self, chain_id, block_id, data, prev_hash):
        self.__chain_id = chain_id
        self.__block_id = block_id
        self.__data = data
        self.__prev_hash = prev_hash
        self.__created_at = datetime.utcnow()
        self.__mine()

    def __mine(self):
        tmp_hash = ''
        i = 0
        re_object = re.compile("^"+VALID_SIGNATURE, re.IGNORECASE)
        partial_str = str(self.__block_id)+str(self.__data)+self.__prev_hash
        while not re_object.match(tmp_hash):
            tmp_hash = hashlib.sha256(partial_str+str(i)).hexdigest()
            if re_object.match(tmp_hash):
                self.__nonce = i
                break
            i += 1

    def get_id(self):
        return self.__block_id

    def get_data(self):
        return self.__data

    def get_prev_hash(self):
        return self.__prev_hash

    def get_nonce(self):
        return self.__nonce

    def get_datetime(self):
        return self.__created_at

    def get_chain_id(self):
        return self.__chain_id

    def get_hash(self):
        return hashlib.sha256(str(self.__block_id)+str(self.__data) +
                              self.__prev_hash+str(self.__nonce)).hexdigest()


class Blockchain:

    def __init__(self):
        self.__chain_id = uuid.uuid1()